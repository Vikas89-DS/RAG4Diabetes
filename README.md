<h1>RAG4Diabetes</h1>

<p>
<b>RAG4Diabetes</b> is a production-oriented Retrieval-Augmented Generation (RAG) system
designed to answer diabetes-related questions strictly from curated medical documents.
The system focuses on correctness, idempotent data ingestion, and enterprise-style
retrieval pipelines.
</p>

<hr/>

<h2>Objective</h2>

<p>
The primary objective of this project is to build a reliable and scalable RAG system
capable of answering diabetes-related queries such as:
</p>

<ul>
  <li>Types and classification of diabetes</li>
  <li>Symptoms, risk factors, and complications</li>
  <li>Treatment approaches and management strategies</li>
  <li>Lifestyle guidance and preventive measures</li>
</ul>

<p>
From a learning perspective, this project was built to deeply understand how
<b>production-grade RAG systems</b> are designed using the LlamaIndex framework.
The focus was on implementing real-world patterns such as hybrid retrieval,
reranking, and idempotent ingestion rather than a simplified demo pipeline.
</p>

<hr/>

<h2>System Architecture</h2>

<ul>
  <li><b>Document Loader:</b> Recursively loads documents from a configurable data directory</li>
  <li><b>Chunking:</b> Sentence-based chunking with overlap to preserve semantic continuity</li>
  <li><b>Embeddings:</b> Local Ollama embedding model (<code>nomic-embed-text</code>)</li>
  <li><b>Vector Store:</b> Persistent ChromaDB for long-term vector storage</li>
  <li><b>Retrieval:</b> Hybrid retrieval using Vector Search and BM25</li>
  <li><b>Query Fusion:</b> Fusion of multiple retrievers to improve recall</li>
  <li><b>Re-Ranking:</b> Cross-encoder reranking for selecting the most relevant chunks</li>
  <li><b>LLM:</b> Google Gemini 2.5 Flash for final answer synthesis</li>
</ul>

<hr/>

<h2>Idempotent Data Ingestion</h2>

<p>
The ingestion pipeline is designed to be safely re-run multiple times without
duplicating data inside the vector database.
</p>

<ul>
  <li>Each document chunk is hashed using SHA-256</li>
  <li>Chunk hashes are stored as metadata in ChromaDB</li>
  <li>Existing hashes are checked before embedding</li>
  <li>Only new or unseen chunks are embedded and inserted</li>
</ul>

<p>
This ensures deterministic behavior and allows incremental updates when new
documents are added to the data directory.
</p>

<hr/>

<h2>Retrieval Strategy</h2>

<p>
The system uses a hybrid retrieval approach to balance precision and recall:
</p>

<ul>
  <li>Dense vector retrieval for semantic similarity</li>
  <li>BM25 keyword-based retrieval for lexical matching</li>
  <li>Query Fusion to combine results from multiple retrievers</li>
  <li>Cross-encoder reranking to refine the final context set</li>
</ul>

<p>
This architecture closely mirrors enterprise-grade RAG implementations.
</p>

<hr/>

<h2>Prompt Safety</h2>

<p>
The prompt enforces strict grounding rules to reduce hallucinations:
</p>

<ul>
  <li>Answers are generated only from retrieved document context</li>
  <li>No external or prior knowledge is allowed</li>
  <li>If the answer is not present in the context, the model explicitly states it</li>
</ul>

<p>
This significantly improves answer trustworthiness for medical information.
</p>

<hr/>

<h2>Configuration</h2>

<p>
All configuration is managed via environment variables defined in a <code>.env</code> file:
</p>

<pre>
GEMINI_API_KEY=your_api_key_here
DATA_DIR=path_to_documents
CHROMA_PATH=path_to_chroma_storage
COLLECTION_NAME=rag4diabetes
</pre>

<p>
This design makes the project portable across local environments, Docker setups,
and cloud deployments.
</p>

<hr/>

<h2>Query Execution</h2>

<p>
The system exposes a single public query interface:
</p>

<pre>
run_query("Your diabetes-related question here")
</pre>

<p>
The function returns the full LlamaIndex response object, including retrieved
source nodes, making it suitable for:
</p>

<ul>
  <li>Streamlit user interfaces</li>
  <li>FastAPI or backend services</li>
  <li>Evaluation pipelines (RAGAS)</li>
  <li>Jupyter notebook experimentation</li>
</ul>

<hr/>

<h2>Use Cases</h2>

<ul>
  <li>Medical document question answering</li>
  <li>Healthcare knowledge assistants</li>
  <li>Enterprise RAG prototypes</li>
  <li>Reference implementation for hybrid RAG systems</li>
</ul>

<hr/>

<h2>Tech Stack</h2>

<ul>
  <li>Python</li>
  <li>LlamaIndex</li>
  <li>ChromaDB</li>
  <li>Ollama (Embeddings)</li>
  <li>Google Gemini 2.5 Flash</li>
  <li>BM25 + Query Fusion</li>
</ul>

<hr/>

<h2>Project Philosophy</h2>

<ul>
  <li>Idempotent and deterministic pipelines</li>
  <li>Production-style retrieval and ranking</li>
  <li>Low hallucination risk by design</li>
  <li>Clean, readable, and extensible codebase</li>
</ul>

<p>
The project intentionally avoids unnecessary complexity while still reflecting
real-world RAG engineering practices.
</p>

