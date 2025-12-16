<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>RAG4Diabetes – Production-Ready RAG System</title>
  <style>
    body {
      font-family: Arial, Helvetica, sans-serif;
      max-width: 900px;
      margin: auto;
      padding: 24px;
      line-height: 1.6;
      color: #1f2937;
    }
    h1, h2, h3 {
      color: #0f4c81;
    }
    code {
      background: #f3f4f6;
      padding: 2px 6px;
      border-radius: 4px;
      font-size: 0.95em;
    }
    pre {
      background: #f9fafb;
      padding: 12px;
      border-radius: 6px;
      overflow-x: auto;
    }
    .box {
      background: #eef5ff;
      border-left: 4px solid #0f4c81;
      padding: 14px;
      margin: 18px 0;
    }
    ul {
      margin-left: 20px;
    }
    hr {
      margin: 32px 0;
    }
  </style>
</head>
<body>

<h1>RAG4Diabetes</h1>

<p>
<b>RAG4Diabetes</b> is a <b>production-ready Retrieval-Augmented Generation (RAG)</b> system
designed to answer diabetes-related medical questions strictly from provided documents.
The system focuses on correctness, reproducibility, and clean engineering practices.
</p>

<hr>

<h2>Why This Project Exists</h2>

<p>
Medical documents such as guidelines, PDFs, and reports are large and unstructured.
Simple keyword search fails to capture context, while naive LLM usage risks hallucination.
</p>

<p>
This project solves the problem by:
</p>

<ul>
  <li>Grounding every answer in retrieved document context</li>
  <li>Preventing duplicate embeddings using idempotent ingestion logic</li>
  <li>Using hybrid retrieval to improve recall and precision</li>
</ul>

<hr>

<h2>System Architecture</h2>

<ul>
  <li><b>Document Loader:</b> Recursively loads PDFs and text files from a configurable directory</li>
  <li><b>Chunking:</b> Sentence-aware chunking with overlap for better semantic continuity</li>
  <li><b>Embeddings:</b> Local Ollama embedding model (cost-efficient and offline-friendly)</li>
  <li><b>Vector Store:</b> Persistent ChromaDB for long-term storage</li>
  <li><b>Retrieval:</b> Hybrid retrieval using Vector Search + BM25</li>
  <li><b>Query Fusion:</b> Multi-query expansion to improve recall</li>
  <li><b>Re-Ranking:</b> LLM-based reranking to select the most relevant chunks</li>
</ul>

<hr>

<h2>Idempotent Data Ingestion</h2>

<div class="box">
This project is designed to be safely re-run multiple times without corrupting
or duplicating the vector database.
</div>

<p>
Key idempotency guarantees:
</p>

<ul>
  <li>Each chunk is hashed using SHA-256</li>
  <li>Chunk hashes are stored as metadata inside ChromaDB</li>
  <li>On every run, existing hashes are checked before embedding</li>
  <li>Only new or unseen chunks are embedded and inserted</li>
</ul>

<p>
As a result:
</p>

<ul>
  <li>Re-running the script does not recreate embeddings</li>
  <li>Existing data remains untouched</li>
  <li>New documents are incrementally indexed</li>
</ul>

<hr>

<h2>Prompt Safety</h2>

<p>
The system enforces strict prompt rules:
</p>

<ul>
  <li>Answers must be generated only from retrieved context</li>
  <li>No external knowledge is allowed</li>
  <li>If information is missing, the model must explicitly state it</li>
</ul>

<p>
This significantly reduces hallucination and improves trustworthiness.
</p>

<hr>

<h2>Configuration</h2>

<p>
All configuration is managed via a <code>.env</code> file:
</p>

<pre>
DATA_DIR=./data
CHROMA_PATH=./chroma_db
COLLECTION_NAME=diabetes_vectors
GEMINI_API_KEY=your_api_key_here
</pre>

<p>
This makes the project portable across environments (local, Docker, cloud).
</p>

<hr>

<h2>Query Execution</h2>

<p>
The core query interface is exposed via a single function:
</p>

<pre>
run_query("Your medical question here")
</pre>

<p>
This design allows easy integration with:
</p>

<ul>
  <li>Streamlit UI</li>
  <li>FastAPI backend</li>
  <li>Evaluation scripts</li>
  <li>Jupyter notebooks</li>
</ul>

<hr>

<h2>Use Cases</h2>

<ul>
  <li>Medical document question answering</li>
  <li>Healthcare knowledge assistants</li>
  <li>Research and guideline exploration</li>
  <li>RAG architecture reference implementation</li>
</ul>

<hr>

<h2>Tech Stack</h2>

<ul>
  <li>Python</li>
  <li>LlamaIndex</li>
  <li>ChromaDB</li>
  <li>Ollama (Embeddings)</li>
  <li>Google Gemini (LLM)</li>
  <li>Streamlit (UI layer)</li>
</ul>

<hr>

<h2>Project Philosophy</h2>

<p>
This project prioritizes:
</p>

<ul>
  <li>Clean and readable code</li>
  <li>Deterministic behavior</li>
  <li>Production-oriented design</li>
  <li>Ease of extension and deployment</li>
</ul>

<p>
It is intentionally kept simple while still reflecting real-world RAG engineering practices.
</p>

</body>
</html>
