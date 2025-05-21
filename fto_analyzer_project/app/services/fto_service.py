from typing import Dict, Any, List
from app.services.weaviate_service import WeaviateClient
from app.services.llm_service import LLMService

class FTOService:
    def __init__(
        self,
        weaviate_url: str,
        weaviate_api_key: str,
        openai_api_key: str,
        model: str,
        temperature: float,
        max_tokens: int,
    ):
        self.weaviate_client = WeaviateClient(
            url=weaviate_url,
            api_key=weaviate_api_key
        )
        self.llm_service = LLMService(
            api_key=openai_api_key,
            model=model,
            temperature=temperature,
            max_tokens=max_tokens,
        )

    def perform_analysis(
        self,
        third_party_claim: str,
        user_description: str,
        top_k: int = 5
    ) -> Dict[str, Any]:
        """
        Retrieve context chunks, build prompt and invoke LLM to perform FTO analysis.
        Returns a dict with keys: decomposition, risks, design_around, technical_rationale.
        """
        # Retrieve relevant chunks
        chunks = self.weaviate_client.retrieve(
            query=third_party_claim,
            top_k=top_k
        )
        # Generate analysis via LLM
        analysis = self.llm_service.generate_analysis(
            third_party_claim=third_party_claim,
            user_description=user_description,
            context_chunks=chunks
        )
        return analysis
