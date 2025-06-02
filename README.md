# 🧠 Diabetes RAG Chatbot (Retrieval-Augmented Generation)

A specialized Question Answering system for healthcare that leverages RAG (Retrieval-Augmented Generation) architecture to answer diabetes-related queries using PDF-based documents.

---

## 🚀 Project Overview

This project implements a **RAG pipeline** using:

- **Document Loaders** to read healthcare PDFs.
- **Text Splitters** to chunk large text into manageable segments.
- **Embeddings** via `nomic-embed-text` (Ollama) to convert text into vector format.
- **Qdrant Vector Store** to store and retrieve chunks efficiently.
- **LLM** (`llama3.2`) to generate answers from retrieved chunks.
- A **QA Chain** to interactively answer user questions.

---

## 🗂️ Project Structure

```bash
├── docs/                    # Folder containing PDF documents
├── main.ipynb              # Main Jupyter Notebook (RAG pipeline)
├── requirements.txt        # Required Python libraries
└── README.md               # Project documentation (you are here)
