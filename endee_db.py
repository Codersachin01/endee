import sys
import os


# Adding path of Endee repo
sys.path.append(os.path.join(os.path.dirname(__file__), "endee"))


class EndeeDB:
    def __init__(self):
        self.data = []

    def add(self, text, embedding):
        self.data.append({"text": text, "embedding": embedding})

    def search(self, query_embedding, top_k=3):
        import numpy as np
        results = []

        for item in self.data:
            score = np.dot(query_embedding, item["embedding"]) / (
                np.linalg.norm(query_embedding) * np.linalg.norm(item["embedding"])
            )
            results.append((item["text"], score))

        results.sort(key=lambda x: x[1], reverse=True)
        return results[:top_k]