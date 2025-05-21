from pydantic import BaseModel, Field
from typing import Optional, List, Dict

class ConfigRequest(BaseModel):
    weaviate_url: str = Field(..., description="URL of the Weaviate instance")
    weaviate_api_key: Optional[str] = Field(None, description="API key for Weaviate")

class IndexRequest(BaseModel):
    file_path: str = Field(..., description="Path to the text file to index")
    batch: bool = Field(False, description="Whether to index in batch mode")

class RetrieveRequest(BaseModel):
    query: str = Field(..., description="Textual query for retrieval")
    top_k: int = Field(5, description="Number of top results to return")
    filters: Optional[Dict[str, str]] = Field(None, description="Metadata filters")

class AnalyzeRequest(BaseModel):
    third_party_claim: str = Field(..., description="Claim text of third-party patent")
    user_description: str = Field(..., description="User's product/process description")
    top_k: int = Field(5, description="Number of context chunks to include")

class Chunk(BaseModel):
    id: str
    content: str
    metadata: Dict[str, str]

class AnalyzeResponse(BaseModel):
    decomposition: str = Field(..., description="Decomposed elements of the claim")
    risks: str = Field(..., description="Potential infringement risks")
    design_around: str = Field(..., description="Suggested design-around modifications")
    technical_rationale: str = Field(..., description="Technical rationale for suggestions")
