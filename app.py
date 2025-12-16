import streamlit as st
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
    Ask questions related to **diabetes mellitus**.  
    Answers are generated **only from the indexed documents**.
    """
)

# ---------------- Input ----------------
query = st.text_area(
    "Enter your question:",
    placeholder="e.g. What are the main types of diabetes mellitus?",
    height=100
)

# ---------------- Button ----------------
if st.button("Ask"):
    if not query.strip():
        st.warning("Please enter a valid question.")
    else:
        with st.spinner("Searching knowledge base..."):
            try:
                response = run_query(query)

                # -------- Answer --------
                st.subheader("Answer")
                st.write(response.response)

                # -------- Sources --------
                if response.source_nodes:
                    st.subheader("Source Contexts")
                    for i, node in enumerate(response.source_nodes, start=1):
                        with st.expander(f"Context {i}"):
                            st.write(node.node.get_content())

            except Exception as e:
                st.error("Something went wrong while generating the answer.")
                st.exception(e)

# ---------------- Footer ----------------
st.markdown("---")
st.caption("RAG4Diabetes | Retrieval-Augmented Generation")