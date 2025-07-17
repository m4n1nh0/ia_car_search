from app.agent.sys_agent import SysAgent
from app.infra.llm.openai_client import OpenAIClient
from app.infra.llm.claude_client import ClaudeClient
from app.infra.mcp.client import filters_results


def main():
    print("\n" + "=" * 60)
    print("🚗  Bem-vindo ao IA Car Search!")
    print("Digite o que você procura (ex: \"Quero um SUV 2020 prata\")")
    print("Ou digite 'sair' para encerrar.\n" + "=" * 60 + "\n")

    openai_llm = OpenAIClient()
    claude_llm = ClaudeClient()
    agent = SysAgent(extractor=openai_llm, responder=claude_llm)

    while True:
        user_input = input("🧑 Você: ").strip()
        if user_input.lower() in ["sair", "exit", "quit"]:
            print("\n👋 Encerrando conversa. Até logo!\n")
            break

        print("\n🤖 IA: Processando sua solicitação...\n")

        filtros = agent.extrair_filtros(user_input)
        print(f"🧠 Filtros extraídos: {filtros}")

        resultados = filters_results(filtros)
        print("🔎 Buscando veículos correspondentes...")

        resposta = agent.gerar_resposta(resultados)
        print(f"\n🤖 IA:\n{resposta}\n")

        print("-" * 60)


if __name__ == "__main__":
    main()
