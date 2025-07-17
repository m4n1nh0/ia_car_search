DEFAULT_EXTRACTION_PROMPT = """
Usuário: {user_input}

Extraia os filtros da frase acima no formato JSON:
{
  "marca": ...,
  "modelo": ...,
  "ano": ...,
  "combustivel": ...
}
"""
