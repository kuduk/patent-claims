from fastapi import APIRouter, HTTPException
from app.api.v1.schemas import ConfigRequest
from app.core.config import settings

router = APIRouter()

@router.post("/", summary="Set or update configuration for Weaviate and LLM")
def update_config(payload: ConfigRequest):
    try:
        # Update runtime settings (in-memory)
        settings.WEAVIATE_URL = payload.weaviate_url
        settings.WEAVIATE_API_KEY = payload.weaviate_api_key
        return {"message": "Configuration updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
