<h1>RAG4Diabetes</h1>

<p>
<b>RAG4Diabetes</b> is a production-oriented <b>Retrieval-Augmented Generation (RAG)</b> project
focused on answering questions from <b>diabetes-related medical documents</b>.
The system is designed to generate accurate, context-grounded answers
strictly based on indexed source documents.
</p>

<hr/>

<h2>Project Overview</h2>

<p>
This project demonstrates how to design a clean and reliable RAG pipeline
that can ingest large medical documents, store them efficiently,
retrieve relevant information, and generate concise answers using an LLM.
</p>

<p>
A key goal of the system is to ensure that responses are grounded in retrieved
context only, avoiding hallucinations or use of external knowledge.
</p>

<hr/>

<h2>High-Level Architecture</h2>

<pre>
Medical Documents (PDF / Text)
        ↓
Idempotent Ingestion (hash-based)
        ↓
Sentence-Based Chunking
        ↓
Vector Embeddings
        ↓
Persistent Vector Store (ChromaDB)
        ↓
Semantic Retrieval
        ↓
Context-Grounded Answer Generation
</pre>

<hr/>

<h2>Key Design Principles</h2>

<ul>
  <li>
    <b>Idempotent Ingestion:</b>
    Documents and chunks are hashed to prevent duplicate processing
    during repeated runs.
  </li>
  <li>
    <b>Persistent Storage:</b>
    Vector embeddings are stored in a persistent database,
    ensuring data survives application restarts.
  </li>
  <li>
    <b>Context-Only Answers:</b>
    The language model is explicitly instructed to answer
    only using retrieved document context.
  </li>
  <li>
    <b>Production-Oriented Design:</b>
    Emphasis is placed on clarity, reproducibility,
    and predictable system behavior.
  </li>
</ul>

<hr/>

<h2>Technology Stack</h2>

<ul>
  <li><b>Language Model:</b> Gemini (Google)</li>
  <li><b>Embeddings:</b> Ollama (nomic-embed-text)</li>
  <li><b>Vector Database:</b> ChromaDB</li>
  <li><b>RAG Framework:</b> LlamaIndex</li>
</ul>

<hr/>

<h2>Project Structure</h2>

<pre>
RAG4Diabetes/
│
├── rag4diabetes.py    # Core RAG pipeline (ingestion, retrieval, generation)
├── data/              # Input medical documents
├── chroma_db/         # Persistent vector store
├── requirements.txt
└── README.md
</pre>

<hr/>

<h2>How to Run</h2>

<h3>1. Install Dependencies</h3>

<pre>
pip install -r requirements.txt
</pre>

<h3>2. Set Environment Variables</h3>

<pre>
GEMINI_API_KEY=your_api_key_here
</pre>

<h3>3. Run the Application</h3>

<pre>
python rag4diabetes.py
</pre>

<hr/>

<h2>Why This Project Matters</h2>

<ul>
  <li>Demonstrates real-world RAG design beyond basic demos</li>
  <li>Handles incremental document updates correctly</li>
  <li>Focuses on reliability and grounded responses</li>
  <li>Can serve as a foundation for enterprise knowledge systems</li>
</ul>

<hr/>

<p>
<b>Note:</b><br/>
For clarity and ease of review, the pipeline is intentionally kept in a single file.
In production environments, the same logic can be modularized without changing
the overall design.
</p>
