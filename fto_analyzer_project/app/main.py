from fastapi import FastAPI
from app.api.v1.endpoints import (
    config_router,
    indexing_router,
    retrieval_router,
    analysis_router,
)

app = FastAPI(title="FTO Analyzer", version="0.1.0")

app.include_router(
    config_router.router,
    prefix="/api/v1/config",
    tags=["config"],
)
app.include_router(
    indexing_router.router,
    prefix="/api/v1/index",
    tags=["indexing"],
)
app.include_router(
    retrieval_router.router,
    prefix="/api/v1/retrieve",
    tags=["retrieval"],
)
app.include_router(
    analysis_router.router,
    prefix="/api/v1/analyze",
    tags=["analysis"],
)
