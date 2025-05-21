from fastapi import APIRouter, HTTPException
from app.api.v1.schemas import IndexRequest
from app.services.document_processor import process_and_chunk
from app.services.weaviate_service import WeaviateClient
from app.core.config import settings

router = APIRouter()

@router.post("/", summary="Index document(s) into Weaviate")
def index_documents(payload: IndexRequest):
    """
    Process a document (or batch of documents) into semantic chunks
    and index them in Weaviate.
    """
    try:
        client = WeaviateClient(
            url=settings.WEAVIATE_URL,
            api_key=settings.WEAVIATE_API_KEY
        )
        client.create_schema()
        chunks = process_and_chunk(payload.file_path, batch=payload.batch)
        client.add_chunks(chunks)
        return {"message": f"Indexed {len(chunks)} chunks successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
