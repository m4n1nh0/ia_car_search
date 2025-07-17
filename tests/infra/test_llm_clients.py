from unittest.mock import patch, MagicMock
from app.infra.llm.openai_client import OpenAIClient
from app.infra.llm.claude_client import ClaudeClient


def test_openai_extract_filters():
    mock_chat = MagicMock()
    mock_chat.choices = [MagicMock()]
    mock_chat.choices[0].message.content = '{"marca": "Toyota", "modelo": "Corolla"}'

    with patch("app.infra.llm.openai_client.OpenAI") as MockOpenAI:
        instance = MockOpenAI.return_value
        instance.chat.completions.create.return_value = mock_chat

        client = OpenAIClient()
        resultado = client.extract_filters("Quero um Corolla da Toyota.")
        assert resultado == {"marca": "Toyota", "modelo": "Corolla"}


def test_claude_generate_response():
    mock_text = MagicMock()
    mock_text.text = "Aqui estão os carros disponíveis..."

    mock_response = MagicMock()
    mock_response.content = [mock_text]

    with patch("app.infra.llm.claude_client.Anthropic") as MockAnthropic:
        instance = MockAnthropic.return_value
        instance.messages.create.return_value = mock_response

        client = ClaudeClient()
        resposta = client.generate_response({"total": 2, "carros": []})
        assert "carros disponíveis" in resposta