from anthropic import Anthropic
from app.utils.config import settings


class ClaudeClient:
    def __init__(self):
        self.client = Anthropic(api_key=settings.CLAUDE_API_KEY)
        self.models = ["claude-sonnet-4-20250514", "claude-opus-4-20250514", "claude-3-5-haiku-20241022"]

    def generate_response(self, data: dict) -> str:
        prompt = (
            "Você é um atendente especializado em vendas de carros.\n"
            "Receberá uma lista de veículos e o total de resultados encontrados.\n\n"
            "Formato esperado da resposta:\n"
            "- Saudação simpática\n"
            "- Quantidade de resultados encontrados\n"
            "- Lista com os principais carros (modelo, ano, motorização, transmissão, cor, preço)\n"
            "- Sugestão para nova busca ou ajuda adicional\n\n"
            "Exemplo de formato:\n"
            "1. Toyota Corolla 2020 - 2.0 Flex, Automático, Prata - R$ 89.000\n"
            "2. Honda HR-V 2019 - 1.8 Flex, Automático, Cinza - R$ 94.000\n\n"
            f"Dados recebidos:\n{data}\n"
            "Gere a resposta agora:"
        )

        for model in self.models:
            try:
                response = self.client.messages.create(
                    model=model,
                    max_tokens=300,
                    temperature=0.5,
                    messages=[{"role": "user", "content": prompt}]
                )
                return response.content[0].text
            except Exception as err:
                print(err)
                continue

        raise RuntimeError("Nenhum modelo Claude disponível para sua conta.")

