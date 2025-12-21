<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <title>RAG4Diabetes – Idempotent RAG System</title>
  <style>
    body {
      font-family: Arial, Helvetica, sans-serif;
      line-height: 1.6;
      color: #1f2937;
      max-width: 900px;
      margin: 40px auto;
      padding: 0 20px;
      background: #ffffff;
    }

    h1, h2, h3 {
      color: #111827;
      border-bottom: 1px solid #e5e7eb;
      padding-bottom: 6px;
    }

    h1 {
      font-size: 32px;
    }

    h2 {
      margin-top: 32px;
    }

    p {
      margin: 12px 0;
    }

    ul {
      margin: 12px 0 12px 20px;
    }

    code, pre {
      background: #f3f4f6;
      padding: 10px;
      display: block;
      border-radius: 6px;
      overflow-x: auto;
      font-size: 14px;
    }

    .tag {
      display: inline-block;
      background: #e5e7eb;
      padding: 4px 10px;
      margin: 4px 6px 4px 0;
      border-radius: 20px;
      font-size: 13px;
    }

    .section {
      margin-top: 28px;
    }
  </style>
</head>
<body>

  <h1>RAG4Diabetes</h1>
  <p><strong>Idempotent, Production-Style Retrieval Augmented Generation System</strong></p>

  <div class="section">
    <h2>Overview</h2>
    <p>
      RAG4Diabetes is a production-oriented Retrieval Augmented Generation (RAG) system
      designed to answer diabetes-related queries using only retrieved document context.
    </p>
    <p>
      The pipeline is fully idempotent — previously processed document chunks are not
      re-embedded or re-inserted when the pipeline is re-run.
    </p>
  </div>

  <div class="section">
    <h2>Key Features</h2>
    <ul>
      <li>Idempotent ingestion using SHA-256 chunk hashing</li>
      <li>Hybrid retrieval: Vector Search + BM25</li>
      <li>Query Fusion Retriever for improved recall</li>
      <li>Cross-encoder re-ranking for high-quality context selection</li>
      <li>Strict context-only answering to prevent hallucinations</li>
      <li>Persistent vector storage with ChromaDB</li>
      <li>Import-safe design for Streamlit or API usage</li>
    </ul>
  </div>

  <div class="section">
    <h2>Tech Stack</h2>
    <div class="tag">LlamaIndex</div>
    <div class="tag">Gemini 2.5 Flash</div>
    <div class="tag">Google GenAI</div>
    <div class="tag">Ollama</div>
    <div class="tag">nomic-embed-text</div>
    <div class="tag">ChromaDB</div>
    <div class="tag">BM25</div>
    <div class="tag">Query Fusion</div>
    <div class="tag">Cross Encoder Re-Ranking</div>
  </div>

  <div class="section">
    <h2>Architecture Flow</h2>
    <ol>
      <li>Documents are loaded recursively from <code>DATA_DIR</code></li>
      <li>Sentence-level chunking with overlap</li>
      <li>SHA-256 hash generated for every chunk</li>
      <li>Existing chunks are skipped using stored hashes</li>
      <li>Only new chunks are embedded and stored in ChromaDB</li>
      <li>Hybrid retrieval (Vector + BM25) at query time</li>
      <li>Query Fusion combines retriever outputs</li>
      <li>Cross-encoder re-ranking refines final context</li>
      <li>LLM generates answer strictly from retrieved context</li>
    </ol>
  </div>

  <div class="section">
    <h2>Environment Variables</h2>
    <pre>
GEMINI_API_KEY=your_api_key
DATA_DIR=path_to_documents
CHROMA_PATH=path_to_chroma_storage
COLLECTION_NAME=rag4diabetes
    </pre>
  </div>

  <div class="section">
    <h2>Query Interface</h2>
    <p>
      The system exposes a single public function:
    </p>
    <pre>
run_query(query: str)
    </pre>
    <p>
      This function executes the full RAG pipeline and returns the complete
      LlamaIndex response object, including retrieved source nodes.
    </p>
  </div>

  <div class="section">
    <h2>Design Philosophy</h2>
    <ul>
      <li>Idempotency-first ingestion</li>
      <li>Enterprise-grade retrieval pipeline</li>
      <li>Low hallucination risk by design</li>
      <li>Clean separation of ingestion and querying</li>
    </ul>
  </div>

  <div class="section">
    <h2>Use Cases</h2>
    <ul>
      <li>Medical domain question answering</li>
      <li>Enterprise document intelligence</li>
      <li>RAG experimentation and evaluation</li>
      <li>LLM system design demonstrations</li>
    </ul>
  </div>

</body>
</html>
