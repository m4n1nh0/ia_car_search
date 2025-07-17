from app.agent.sys_agent import SysAgent


class MockLLM:
    def extract_filters(self, user_input):
        return {"marca": "Toyota"}

    def generate_response(self, context):
        return f"Mocked {context.get('quantidade')} resultado(s)"


def test_chat_agent_interacao(monkeypatch):
    agent = SysAgent(extractor=MockLLM(), responder=MockLLM())

    inputs = iter(["Quero um Toyota", "sair"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    filtros = agent.extrair_filtros("Quero um Toyota")
    resposta = agent.gerar_resposta([{"modelo": "Corolla"}])

    assert filtros["marca"] == "Toyota"
    assert "Mocked" in resposta
