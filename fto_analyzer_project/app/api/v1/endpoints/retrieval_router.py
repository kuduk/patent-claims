from fastapi import APIRouter, HTTPException
from app.api.v1.schemas import RetrieveRequest, Chunk
from app.services.weaviate_service import WeaviateClient
from app.core.config import settings
from typing import List, Dict

router = APIRouter()

@router.post("/", response_model=List[Chunk], summary="Retrieve relevant document chunks")
def retrieve_chunks(payload: RetrieveRequest):
    try:
        client = WeaviateClient(
            url=settings.WEAVIATE_URL,
            api_key=settings.WEAVIATE_API_KEY
        )
        results = client.retrieve(
            query=payload.query,
            top_k=payload.top_k,
            filters=payload.filters  # type: ignore
        )
        return [Chunk(id=item["id"], content=item["content"], metadata=item["metadata"]) for item in results]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
