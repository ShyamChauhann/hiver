# import numpy as np
# import os
# import joblib
# from sentence_transformers import SentenceTransformer
# from sklearn.metrics.pairwise import cosine_similarity

# class HistoricalRetriever:

#     def __init__(self, dataframe):

#         self.df = dataframe.reset_index(drop=True)

#         self.model = SentenceTransformer(
#             "sentence-transformers/all-MiniLM-L6-v2"
#         )

#         print("saving embeddings as pkl file...")

#         EMBEDDING_FILE = "models/embeddings.pkl"


#         if os.path.exists(EMBEDDING_FILE):

#             print("Loading cached embeddings...")

#             embeddings = joblib.load(EMBEDDING_FILE)

#         else:

#             print("Creating embeddings...")

#             embeddings = model.encode(
#                 texts,
#                 batch_size=32,
#                 show_progress_bar=True
#             )

#             os.makedirs("models", exist_ok=True)

#             joblib.dump(
#                 embeddings,
#                 EMBEDDING_FILE
#             )

#             print("Embeddings saved to:", EMBEDDING_FILE)

#         # self.embeddings = self.model.encode(
#         #     self.df["customer_text"].tolist(),
#         #     normalize_embeddings=True,
#         #     show_progress_bar=True
#         # )

#     def search(
#         self,
#         query,
#         top_k=5
#     ):

#         query_embedding = self.model.encode(
#             [query],
#             normalize_embeddings=True
#         )

#         similarities = cosine_similarity(
#             query_embedding,
#             self.embeddings
#         )[0]

#         indices = np.argsort(
#             similarities
#         )[::-1][:top_k]

#         results = []

#         for index in indices:

#             result = self.df.iloc[index].to_dict()

#             result["similarity"] = float(
#                 similarities[index]
#             )

#             results.append(result)

#         return results


import numpy as np
import os
import joblib

from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


class HistoricalRetriever:

    def __init__(self, dataframe):

        self.df = dataframe.reset_index(drop=True)

        # Load embedding model
        self.model = SentenceTransformer(
            "sentence-transformers/all-MiniLM-L6-v2"
        )

        EMBEDDING_FILE = "models/embeddings.pkl"

        # Get customer texts
        texts = self.df["customer_text"].tolist()

        # Check if cached embeddings already exist
        if os.path.exists(EMBEDDING_FILE):

            print("Loading cached embeddings...")

            self.embeddings = joblib.load(
                EMBEDDING_FILE
            )

        else:

            print("Creating embeddings...")

            self.embeddings = self.model.encode(
                texts,
                batch_size=32,
                normalize_embeddings=True,
                show_progress_bar=True
            )

            # Create models directory
            os.makedirs(
                "models",
                exist_ok=True
            )

            # Save embeddings
            joblib.dump(
                self.embeddings,
                EMBEDDING_FILE
            )

            print(
                "Embeddings saved to:",
                EMBEDDING_FILE
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