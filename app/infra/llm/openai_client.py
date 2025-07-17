from openai import OpenAI
import os
import json

from app.utils.config import settings


class OpenAIClient:
    def __init__(self):
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def extract_filters(self, prompt: str) -> dict:
        """
        Extrai filtros do texto usando OpenAI GPT (formato JSON no retorno).
        """
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system",
                    "content": "Extraia os filtros de busca de carros do texto do usuário no formato JSON. "
                               "Por exemplo: {\"marca\": \"Toyota\", \"modelo\": \"Corolla\"}."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )

        raw_content = response.choices[0].message.content
        try:
            return json.loads(raw_content)
        except json.JSONDecodeError:
            return {}
