import weaviate
from app.core.exceptions import (
    WeaviateConnectionError,
    SchemaCreationError,
    IndexingError,
    RetrievalError,
)
from typing import List, Dict

class WeaviateClient:
    CLASS_NAME = "Chunk"

    def __init__(self, url: str, api_key: str = None):
        try:
            auth = weaviate.auth.AuthApiKey(api_key) if api_key else None
            self.client = weaviate.Client(url=url, auth_client_secret=auth)
        except Exception as e:
            raise WeaviateConnectionError(f"Cannot connect to Weaviate at {url}: {e}")

    def create_schema(self) -> None:
        """
        Create the Chunk class schema if it does not already exist.
        """
        try:
            schema = self.client.schema.get()
            classes = [c["class"] for c in schema.get("classes", [])]
            if self.CLASS_NAME in classes:
                return
            class_obj = {
                "class": self.CLASS_NAME,
                "vectorizer": "text2vec-openai",
                "properties": [
                    {"name": "content", "dataType": ["text"]},
                    {"name": "metadata", "dataType": ["text"]},
                ],
            }
            self.client.schema.create_class(class_obj)
        except Exception as e:
            raise SchemaCreationError(f"Failed to create schema: {e}")

    def add_chunks(self, chunks: List[Dict]) -> None:
        """
        Add a list of chunk dicts to Weaviate.
        Each dict must contain 'id', 'content', and 'metadata'.
        """
        try:
            for chunk in chunks:
                obj = {
                    "content": chunk["content"],
                    "metadata": str(chunk.get("metadata", {})),
                }
                self.client.data_object.create(
                    data_object=obj,
                    class_name=self.CLASS_NAME,
                    uuid=chunk["id"],
                )
        except Exception as e:
            raise IndexingError(f"Failed to index chunks: {e}")

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
        filters: Dict[str, str] = None,
    ) -> List[Dict]:
        """
        Retrieve relevant chunks using nearText and optional metadata filters.
        Returns list of dicts with keys 'id', 'content', 'metadata'.
        """
        try:
            builder = (
                self.client.query
                .get(self.CLASS_NAME, ["content", "metadata"])
                .with_near_text({"concepts": [query]})
                .with_limit(top_k)
            )
            if filters:
                # simple filter: metadata text contains filter values
                for key, value in filters.items():
                    builder = builder.with_additional(
                        {"filter": { "path": ["metadata"], "operator": "Like", "valueText": value }}
                    )
            results = builder.do()
            return [
                {
                    "id": r["id"],
                    "content": r["properties"]["content"],
                    "metadata": r["properties"]["metadata"],
                }
                for r in results.get("data", {}).get("Get", {}).get(self.CLASS_NAME, [])
            ]
        except Exception as e:
            raise RetrievalError(f"Failed to retrieve chunks: {e}")
