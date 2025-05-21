import json
from typing import List, Dict, Any
from langchain.llms import OpenAI
from app.core.exceptions import LLMError

class LLMService:
    def __init__(
        self,
        api_key: str,
        model: str = "gpt-4",
        temperature: float = 0.7,
        max_tokens: int = 1024,
    ):
        try:
            self.llm = OpenAI(
                openai_api_key=api_key,
                model_name=model,
                temperature=temperature,
                max_tokens=max_tokens,
            )
        except Exception as e:
            raise LLMError(f"Failed to initialize LLM client: {e}")

    def generate_analysis(
        self,
        third_party_claim: str,
        user_description: str,
        context_chunks: List[Dict[str, Any]],
    ) -> Dict[str, Any]:
        """
        Build prompt and call the LLM to perform FTO analysis.
        Expects the LLM to return a JSON string with keys:
        decomposition, risks, design_around, technical_rationale.
        """
        prompt = (
            "You are an expert in chemical patents and freedom to operate analysis.\n\n"
            f"Third-party claim:\n{third_party_claim}\n\n"
            f"User's product/process description:\n{user_description}\n\n"
            "Context chunks from patent database:\n"
        )
        for chunk in context_chunks:
            prompt += f"- {chunk['id']}: {chunk['content']}\n"
        prompt += (
            "\nPlease perform the following:\n"
            "1. Decompose the third-party claim into its essential elements.\n"
            "2. Identify potential infringement risks by comparing with the user's description.\n"
            "3. Suggest specific design-around modifications to avoid literal coverage.\n"
            "4. Provide technical/chemical rationale for each suggestion.\n\n"
            "Return your answer as a JSON object with the following keys:\n"
            "decomposition, risks, design_around, technical_rationale.\n"
        )
        try:
            raw = self.llm(prompt)
            return json.loads(raw)
        except Exception as e:
            raise LLMError(f"LLM generation failed: {e}")
