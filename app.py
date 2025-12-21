import streamlit as st
from pathlib import Path
from dotenv import load_dotenv

# ---------------- Ensure .env loads correctly ----------------
env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

from rag4diabetes import run_query

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="RAG4Diabetes",
    page_icon="🩺",
    layout="centered"
)

# ---------------- Title ----------------
st.title("RAG4Diabetes")
st.caption("Diabetes knowledge assistant powered by Retrieval-Augmented Generation")

# ---------------- Instructions ----------------
st.markdown(
    """
    Ask questions related to **Diabetes**.  
    Answers are generated **only from the indexed documents** (no external knowledge).
    """
)

# ---------------- Input ----------------
query = st.text_area(
    "Enter your question:",
    placeholder="e.g. What are the main types of diabetes mellitus?",
    height=100
)

# ---------------- Cached Query Wrapper ----------------
@st.cache_data(show_spinner=False)
def cached_query(q: str):
    return run_query(q)

# ---------------- Button ----------------
if st.button("Ask"):
    if not query.strip():
        st.warning("Please enter a valid question.")
    else:
        with st.spinner("Searching knowledge base..."):
            try:
                response = cached_query(query)

                # -------- Answer --------
                st.subheader("Answer")
                st.write(response.response)

                # -------- Sources (Optional / Expandable) --------
                if response.source_nodes:
                    with st.expander("View source contexts"):
                        for i, node in enumerate(response.source_nodes, start=1):
                            st.markdown(f"**Context {i}**")
                            st.write(node.node.get_content())

            except Exception as e:
                st.error("Something went wrong while generating the answer.")
                st.exception(e)

# ---------------- Footer ----------------
st.markdown("---")
st.caption("RAG4Diabetes | RAG system with hybrid retrieval & cross-encoder reranking")
