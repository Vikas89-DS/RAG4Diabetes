# =========================
# RAG4Diabetes - Idempotent Dev Script
# =========================

import os
import hashlib
from dotenv import load_dotenv
import nest_asyncio
nest_asyncio.apply()

# =========================
# Load Environment Variables
# =========================

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
DATA_DIR = os.getenv("DATA_DIR")
CHROMA_PATH = os.getenv("CHROMA_PATH")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")

if not DATA_DIR or not CHROMA_PATH or not COLLECTION_NAME:
    raise ValueError("DATA_DIR, CHROMA_PATH, or COLLECTION_NAME missing in .env file")

# =========================
# LlamaIndex Imports
# =========================

from llama_index.core import (
    SimpleDirectoryReader,
    VectorStoreIndex,
    Settings,
    StorageContext,
    PromptTemplate,
)
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.retrievers import QueryFusionRetriever
from llama_index.retrievers.bm25 import BM25Retriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.postprocessor import SentenceTransformerRerank

from llama_index.llms.google_genai import GoogleGenAI
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.vector_stores.chroma import ChromaVectorStore

import chromadb

# =========================
# Global Models
# =========================

embed_model = OllamaEmbedding(
    model_name="nomic-embed-text:latest",
    base_url="http://localhost:11434",
)

llm = GoogleGenAI(
    model="models/gemini-2.5-flash",
    temperature= 0.3,
    api_key=GEMINI_API_KEY,
)

Settings.embed_model = embed_model
Settings.llm = llm

# =========================
# Utility: Hashing
# =========================

def sha256(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

# =========================
# Load Documents
# =========================

documents = SimpleDirectoryReader(
    DATA_DIR,
    recursive=True
).load_data()

splitter = SentenceSplitter(
    chunk_size=256,
    chunk_overlap=25
)

nodes = splitter.get_nodes_from_documents(documents)

# =========================
# Chroma Setup
# =========================

chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = chroma_client.get_or_create_collection(
    name=COLLECTION_NAME
)

# =========================
# Idempotency Check
# =========================

existing = collection.get(include=["metadatas"])
existing_chunk_hashes = set()

for meta in existing.get("metadatas", []):
    if meta and "chunk_hash" in meta:
        existing_chunk_hashes.add(meta["chunk_hash"])

# =========================
# Filter New Nodes Only
# =========================

new_nodes = []

for node in nodes:
    content = node.get_content()
    chunk_hash = sha256(content)

    if chunk_hash in existing_chunk_hashes:
        continue

    node.metadata["chunk_hash"] = chunk_hash
    node.metadata["source"] = node.metadata.get("file_name", "unknown")
    new_nodes.append(node)

print(f"Total chunks found   : {len(nodes)}")
print(f"New chunks inserted  : {len(new_nodes)}")

# =========================
# Vector Store Index
# =========================

vector_store = ChromaVectorStore(
    chroma_collection=collection
)

storage_context = StorageContext.from_defaults(
    vector_store=vector_store
)

if new_nodes:
    index = VectorStoreIndex(
        nodes=new_nodes,
        storage_context=storage_context,
    )
else:
    index = VectorStoreIndex.from_vector_store(
        vector_store=vector_store
    )

# =========================
# Prompt Template
# =========================

qa_prompt = PromptTemplate(
    "Context:\n{context_str}\n\n"
    "Instructions:\n"
    "- Answer using ONLY the information from the context.\n"
    "- Do NOT use external knowledge.\n"
    "- Combine and synthesize information from multiple context passages if needed.\n"
    "- Write the answer as a clear, professional advisory explanation in paragraph form.\n\n"
    "Query: {query_str}\n"
    "Answer:"
)

# =========================
# Retrievers
# =========================

vector_retriever = index.as_retriever(similarity_top_k=10)

bm25_retriever = BM25Retriever.from_defaults(
    nodes=nodes,
    similarity_top_k=10
)

fusion_retriever = QueryFusionRetriever(
    retrievers=[vector_retriever, bm25_retriever],
    similarity_top_k=10,
    num_queries=1,
    use_async=True,
)

# =========================
# Re-ranker
# =========================

reranker = SentenceTransformerRerank(
    model="cross-encoder/ms-marco-MiniLM-L-6-v2",
    top_n=10
)

# =========================
# Query Engine
# =========================

query_engine = RetrieverQueryEngine.from_args(
    retriever=fusion_retriever,
    node_postprocessors=[reranker],
)

query_engine.update_prompts({
    "response_synthesizer:text_qa_template": qa_prompt
})

# =========================
# Public Function (Import-safe)
# =========================

def run_query(query: str):
    """
    Executes a query against the RAG system.
    Returns the full LlamaIndex response object.
    """
    return query_engine.query(query)