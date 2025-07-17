class SysAgent:
    def __init__(self, extractor, responder):
        self.extractor = extractor
        self.responder = responder

    def extrair_filtros(self, user_input: str) -> dict:
        return self.extractor.extract_filters(user_input)

    def gerar_resposta(self, resultados: list) -> str:
        contexto = {
            "resultado": resultados,
            "quantidade": len(resultados)
        }
        return self.responder.generate_response(contexto)
