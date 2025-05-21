class WeaviateConnectionError(Exception):
    """Raised when connection to Weaviate fails."""

class SchemaCreationError(Exception):
    """Raised when creating schema in Weaviate fails."""

class IndexingError(Exception):
    """Raised when indexing documents in Weaviate fails."""

class RetrievalError(Exception):
    """Raised when retrieving data from Weaviate fails."""

class LLMError(Exception):
    """Raised when the LLM request or response fails."""

class FTOAnalysisError(Exception):
    """Raised when Freedom to Operate analysis encounters an error."""
