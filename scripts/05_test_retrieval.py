import pandas as pd
import sys

sys.path.append(".")

from src.retrieval import HistoricalRetriever

df = pd.read_csv(
    "dataset/processed/support_pairs.csv"
)

retriever = HistoricalRetriever(df)

query = input(
    "\nEnter customer message: "
)

results = retriever.search(
    query,
    top_k=5
)

print("\nSimilar historical cases:\n")

for i, result in enumerate(results):

    print("=" * 70)

    print(
        f"Similarity: "
        f"{result['similarity']:.3f}"
    )

    print(
        "Customer:",
        result["customer_text"]
    )

    print(
        "Brand:",
        result["brand_response"]
    )