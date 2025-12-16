<h1>RAG4Diabetes</h1>

<p>
A production-oriented <b>Retrieval-Augmented Generation (RAG)</b> application focused on
<b>diabetes-related medical documents</b>.
This project demonstrates how to build a clean, idempotent RAG pipeline with
vector search, reranking, evaluation, and a simple UI.
</p>

<hr/>

<h2>Project Overview</h2>

<p>
The goal of this project is to answer medical questions about
<b>Diabetes Mellitus</b> strictly using information retrieved from
indexed documents — without hallucinating or using external knowledge.
</p>

<ul>
  <li>Incremental & idempotent document ingestion</li>
  <li>Persistent vector database using Chroma</li>
  <li>Semantic retrieval with reranking</li>
  <li>Reference-free RAG evaluation using RAGAS</li>
  <li>Simple Streamlit UI for interaction</li>
</ul>

<hr/>

<h2>High-Level Architecture</h2>

<pre>
Documents (PDF / Text)
        ↓
Idempotent Ingestion (hash-based)
        ↓
Chunking (Sentence Splitter)
        ↓
Vector Embeddings (Ollama)
        ↓
Chroma Vector Store (Persistent)
        ↓
Vector Retrieval (Top-K)
        ↓
LLM Reranking
        ↓
Answer Generation (Gemini)
</pre>

<hr/>

<h2>Key Design Decisions</h2>

<ul>
  <li>
    <b>Idempotent Ingestion:</b>
    Documents and chunks are hashed to avoid duplicate embeddings on re-runs.
  </li>
  <li>
    <b>Persistent Vector Store:</b>
    ChromaDB is used so embeddings survive application restarts.
  </li>
  <li>
    <b>No Hybrid Search (for simplicity):</b>
    BM25 was intentionally removed to keep the pipeline stable and readable.
  </li>
  <li>
    <b>Reference-Free Evaluation:</b>
    RAGAS metrics are used without requiring a labeled ground-truth dataset.
  </li>
</ul>

<hr/>

<h2>Tech Stack</h2>

<ul>
  <li><b>LLM:</b> Gemini (Google)</li>
  <li><b>Embeddings:</b> Ollama (nomic-embed-text)</li>
  <li><b>Vector DB:</b> Chroma</li>
  <li><b>Framework:</b> LlamaIndex</li>
  <li><b>Evaluation:</b> RAGAS</li>
  <li><b>UI:</b> Streamlit</li>
</ul>

<hr/>

<h2>Project Structure</h2>

<pre>
RAG4Diabetes/
│
├── rag4diabetes.py    # Core RAG pipeline (ingestion + retrieval + generation)
├── evaluation.py      # Reference-free RAGAS evaluation
├── app.py             # Streamlit UI
├── data/              # Input documents
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

<h3>3. Run the RAG Pipeline</h3>

<pre>
python rag4diabetes.py
</pre>

<h3>4. Run Evaluation (RAGAS)</h3>

<pre>
python evaluation.py
</pre>

<h3>5. Launch UI</h3>

<pre>
streamlit run app.py
</pre>

<hr/>

<h2>Evaluation Strategy</h2>

<p>
Since no labeled ground-truth dataset is available, the system is evaluated using
<b>reference-free RAGAS metrics</b>:
</p>

<ul>
  <li><b>Faithfulness:</b> Ensures answers are grounded in retrieved context</li>
  <li><b>Answer Relevancy:</b> Measures relevance of the answer to the query</li>
</ul>

<p>
This approach mirrors real-world enterprise RAG systems where labeled data
is often unavailable.
</p>

<hr/>

<h2>Limitations & Future Improvements</h2>

<ul>
  <li>Add hybrid retrieval (BM25 + vectors)</li>
  <li>Introduce agentic RAG for iterative retrieval</li>
  <li>Improve chunking strategy for medical documents</li>
  <li>Add feedback-based evaluation loop</li>
</ul>

<hr/>

<h2>Why This Project Matters</h2>

<ul>
  <li>Shows production thinking beyond simple RAG demos</li>
  <li>Handles idempotency and re-runs correctly</li>
  <li>Includes evaluation — often missing in GenAI projects</li>
  <li>Designed to be easily extensible to enterprise use cases</li>
</ul>

<hr/>

<p>
<b>Note:</b>  
The pipeline is intentionally kept in a single file for clarity and ease of review.
In a production environment, components would be modularized without changing the core logic.
</p>
