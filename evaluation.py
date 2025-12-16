import os
from dotenv import load_dotenv
load_dotenv()

# --------------------------------------------------
# Import RAG pipeline
# --------------------------------------------------
from rag4diabetes import run_query

# --------------------------------------------------
# RAGAS imports
# --------------------------------------------------
from ragas import evaluate
from ragas.metrics import (
    faithfulness,
    answer_relevancy,
)
from datasets import Dataset

# --------------------------------------------------
# Evaluation questions
# --------------------------------------------------
evaluation_questions = [
    "What are the main primary types of diabetes mellitus?",
    "How is diabetes mellitus generally classified?",
    "What distinguishes Type 1 and Type 2 diabetes?",
]

# --------------------------------------------------
# Collect RAG outputs
# --------------------------------------------------
records = []

for question in evaluation_questions:
    response = run_query(question)

    contexts = [
        node.node.get_content()
        for node in response.source_nodes
        if node.node.get_content()
    ]

    if not contexts:
        continue

    records.append({
        "question": question,
        "answer": response.response,
        "contexts": contexts,
    })

# --------------------------------------------------
# Build dataset
# --------------------------------------------------
dataset = Dataset.from_list(records)

# --------------------------------------------------
# Run RAGAS evaluation (simple, default LLM)
# --------------------------------------------------
results = evaluate(
    dataset=dataset,
    metrics=[
        faithfulness,
        answer_relevancy,
    ],
)

# --------------------------------------------------
# Print results
# --------------------------------------------------
print("\nRAGAS Evaluation Results (Reference-Free)\n")
print(results)