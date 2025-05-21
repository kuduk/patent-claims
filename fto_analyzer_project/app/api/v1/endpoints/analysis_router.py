from fastapi import APIRouter, HTTPException
from typing import List
from app.api.v1.schemas import AnalyzeRequest, AnalyzeResponse, Chunk
from app.services.fto_service import FTOService
from app.core.config import settings

router = APIRouter()

@router.post("/", response_model=AnalyzeResponse, summary="Perform FTO analysis")
def analyze(request: AnalyzeRequest):
    """
    Perform Freedom to Operate analysis by:
      - retrieving relevant context chunks
      - generating analysis via LLM
    """
    try:
        service = FTOService(
            weaviate_url=settings.WEAVIATE_URL,
            weaviate_api_key=settings.WEAVIATE_API_KEY,
            openai_api_key=settings.OPENAI_API_KEY,
            model=settings.LLM_MODEL,
            temperature=settings.TEMPERATURE,
            max_tokens=settings.MAX_TOKENS,
        )
        response = service.perform_analysis(
            third_party_claim=request.third_party_claim,
            user_description=request.user_description,
            top_k=request.top_k
        )
        return AnalyzeResponse(
            decomposition=response["decomposition"],
            risks=response["risks"],
            design_around=response["design_around"],
            technical_rationale=response["technical_rationale"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
