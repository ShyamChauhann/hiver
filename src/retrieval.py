import numpy as np

from sentence_transformers import SentenceTransformer

from sklearn.metrics.pairwise import cosine_similarity

class HistoricalRetriever:

    def __init__(self, dataframe):

        self.df = dataframe.reset_index(drop=True)

        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

        print("Creating embeddings...")

        self.embeddings = self.model.encode(
            self.df["customer_text"].tolist(),
            normalize_embeddings=True,
            show_progress_bar=True
        )

    def search(
        self,
        query,
        top_k=5
    ):

        query_embedding = self.model.encode(
            [query],
            normalize_embeddings=True
        )

        similarities = cosine_similarity(
            query_embedding,
            self.embeddings
        )[0]

        indices = np.argsort(
            similarities
        )[::-1][:top_k]

        results = []

        for index in indices:

            result = self.df.iloc[index].to_dict()

            result["similarity"] = float(
                similarities[index]
            )

            results.append(result)

        return results