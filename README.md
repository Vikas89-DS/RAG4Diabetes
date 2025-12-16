<h1>RAG4Diabetes</h1>

<p>
<b>RAG4Diabetes</b> is a production-ready Retrieval-Augmented Generation (RAG) system
designed to answer diabetes-related questions strictly from provided medical documents.
The project emphasizes correctness, reproducibility, and clean engineering practices.
</p>

<hr/>

<h2>Objective</h2>

<p>
The primary objective of this project is to build a RAG-based system that can reliably
provide diabetes-related information, including:
</p>

<ul>
  <li>Types of diabetes</li>
  <li>Risk factors and symptoms</li>
  <li>Treatment approaches</li>
  <li>Lifestyle and health choices for diabetes management</li>
</ul>

<p>
From a personal learning perspective, this project was created to explore the
<b>LlamaIndex framework</b> in depth and to understand how real-world RAG systems are
designed and implemented. The focus was on building a practical, end-to-end RAG pipeline
rather than a simplified or toy implementation.
</p>

<hr/>

<h2>System Architecture</h2>

<ul>
  <li><b>Document Loader:</b> Recursively loads PDFs and text files from a configurable directory</li>
  <li><b>Chunking:</b> Sentence-aware chunking with overlap to preserve semantic context</li>
  <li><b>Embeddings:</b> Local Ollama embedding model for cost-efficient vectorization</li>
  <li><b>Vector Store:</b> Persistent ChromaDB for long-term storage</li>
  <li><b>Retrieval:</b> Hybrid retrieval using Vector Search and BM25</li>
  <li><b>Query Fusion:</b> Multi-query expansion to improve recall</li>
  <li><b>Re-Ranking:</b> LLM-based reranking to select the most relevant chunks</li>
</ul>

<hr/>

<h2>Idempotent Data Ingestion</h2>

<p>
The system is designed to be safely re-run multiple times without duplicating data
or corrupting the vector database.
</p>

<ul>
  <li>Each chunk is hashed using SHA-256</li>
  <li>Chunk hashes are stored as metadata inside ChromaDB</li>
  <li>Existing hashes are checked before embedding</li>
  <li>Only new or unseen chunks are embedded and inserted</li>
</ul>

<p>
This ensures deterministic behavior and allows incremental document updates.
</p>

<hr/>

<h2>Prompt Safety</h2>

<p>
The prompt enforces strict grounding rules:
</p>

<ul>
  <li>Answers are generated only from retrieved document context</li>
  <li>No external or prior knowledge is allowed</li>
  <li>If information is missing, the model explicitly states it</li>
</ul>

<p>
This significantly reduces hallucination and improves trustworthiness.
</p>

<hr/>

<h2>Configuration</h2>

<p>
All configuration is managed through a <code>.env</code> file:
</p>

<pre>
DATA_DIR=./data
CHROMA_PATH=./chroma_db
COLLECTION_NAME=diabetes_vectors
GEMINI_API_KEY=your_api_key_here
</pre>

<p>
This makes the project portable across environments such as local setups, Docker,
and cloud deployments.
</p>

<hr/>

<h2>Query Execution</h2>

<p>
The core query interface is exposed via a single function:
</p>

<pre>
run_query("Your diabetes-related question here")
</pre>

<p>
This design allows easy integration with:
</p>

<ul>
  <li>Streamlit UI</li>
  <li>FastAPI backends</li>
  <li>Evaluation or testing scripts</li>
  <li>Jupyter notebooks</li>
</ul>

<hr/>

<h2>Use Cases</h2>

<ul>
  <li>Medical document question answering</li>
  <li>Healthcare knowledge assistants</li>
  <li>Exploration of diabetes-related guidelines and research</li>
  <li>Reference implementation for RAG architectures</li>
</ul>

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
  <li>Deterministic and idempotent behavior</li>
  <li>Production-oriented design</li>
  <li>Ease of extension and deployment</li>
</ul>

<p>
The project is intentionally kept simple while still reflecting real-world RAG
engineering practices.
</p>
