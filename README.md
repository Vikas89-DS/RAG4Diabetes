<h1>RAG4Diabetes</h1>

<p>
<b>RAG4Diabetes</b> is a production-ready Retrieval-Augmented Generation (RAG) system
designed to answer diabetes-related medical questions strictly from provided documents.
The system focuses on correctness, reproducibility, and clean engineering practices.
</p>

<hr/>

<h2>Why This Project Exists</h2>

<p>
Medical documents such as guidelines, PDFs, and reports are large and unstructured.
Simple keyword search fails to capture context, while naive LLM usage risks hallucination.
</p>

<p>This project solves the problem by:</p>

<ul>
  <li>Grounding every answer in retrieved document context</li>
  <li>Preventing duplicate embeddings using idempotent ingestion logic</li>
  <li>Using hybrid retrieval to improve recall and precision</li>
</ul>

<hr/>

<h2>System Architecture</h2>

<ul>
  <li><b>Document Loader:</b> Recursively loads PDFs and text files</li>
  <li><b>Chunking:</b> Sentence-aware chunking with overlap</li>
  <li><b>Embeddings:</b> Local Ollama embedding model</li>
  <li><b>Vector Store:</b> Persistent ChromaDB</li>
  <li><b>Retrieval:</b> Hybrid (Vector Search + BM25)</li>
  <li><b>Query Fusion:</b> Multi-query expansion</li>
  <li><b>Re-Ranking:</b> LLM-based reranking</li>
</ul>

<hr/>

<h2>Idempotent Data Ingestion</h2>

<p>
This project can be safely re-run multiple times without duplicating embeddings.
</p>

<ul>
  <li>Each chunk is hashed using SHA-256</li>
  <li>Hashes are stored as metadata in ChromaDB</li>
  <li>Only new or unseen chunks are embedded</li>
</ul>

<hr/>

<h2>Configuration</h2>

<pre>
DATA_DIR=./data
CHROMA_PATH=./chroma_db
COLLECTION_NAME=diabetes_vectors
GEMINI_API_KEY=your_api_key_here
</pre>

<hr/>

<h2>Query Execution</h2>

<pre>
run_query("Your medical question here")
</pre>

<hr/>

<h2>Tech Stack</h2>

<ul>
  <li>Python</li>
  <li>LlamaIndex</li>
  <li>ChromaDB</li>
  <li>Ollama (Embeddings)</li>
  <li>Google Gemini (LLM)</li>
  <li>Streamlit</li>
</ul>

<hr/>

<h2>Project Philosophy</h2>

<ul>
  <li>Clean and readable code</li>
  <li>Deterministic behavior</li>
  <li>Production-oriented design</li>
  <li>Easy extensibility</li>
</ul>
