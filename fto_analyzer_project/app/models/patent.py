from pydantic import BaseModel, Field
from typing import List, Dict

class PatentMetadata(BaseModel):
    patent_number: str = Field(..., description="Patent number")
    publication_date: str = Field(..., description="Publication date of the patent")
    applicant: str = Field(..., description="Patent applicant")
    inventors: List[str] = Field(..., description="List of inventors")
    ipc_classes: List[str] = Field(..., description="IPC classification codes")

class PatentDocument(BaseModel):
    metadata: PatentMetadata
    content: str = Field(..., description="Full text content of the patent")
