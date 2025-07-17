# 🚗 IA Car Search

Um sistema conversacional inteligente para busca de veículos via terminal, utilizando LLMs como OpenAI e Claude (Anthropic).

## 🔧 Configuração

1. Crie um arquivo `.env` com suas chaves de API:

```env
OPENAI_API_KEY=your_openai_key
CLAUDE_API_KEY=your_claude_key
````

2. Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

## ▶️ Como Executar

### 1. Popule o banco de dados com dados fictícios:

```bash
python -m scripts.populate_db
```

### 2. Inicie o servidor MCP (Módulo de Consulta Persistente):

```bash
python -m app.infra.mcp.server
```

### 3. Em outro terminal, inicie o agente conversacional:

```bash
python app/main.py
```

## 💬 Exemplo de Uso

```text
============================================================
🚗  Bem-vindo ao IA Car Search!
Digite o que você procura (ex: "Quero um Corolla 2020 prata")
Ou digite 'sair' para encerrar.
============================================================

🧑 Você: Quero um SUV automático da Honda abaixo de 100 mil

🤖 IA: Processando sua solicitação...

🧠 Filtros extraídos: {'marca': 'Honda', 'tipo_carroceria': 'SUV', 'preco_max': 100000}
🔎 Buscando veículos correspondentes...

💬 Resposta da IA:
1. Honda HR-V 2019 - Automático, 45.000km - R$ 89.000 - Prata
2. Honda WR-V 2020 - Automático, 32.000km - R$ 94.000 - Branco

Deseja ver mais detalhes ou buscar novamente?
```

## 🧠 Tecnologias Utilizadas

* **Python 3.11+**
* **OpenAI API (GPT-3.5+)**
* **Claude API (Anthropic)**
* **SQLAlchemy** — ORM para persistência
* **Pydantic** — Validação e serialização de dados
* **Faker** — Geração de dados fictícios
* **Socket** — Comunicação entre serviços

## 📦 Estrutura de Diretórios

```
ia_car_search/
├── app/
│   ├── agent/               # Agente principal com integração LLM
│   ├── domain/              # DTOs, entidades e regras de negócio
│   ├── infra/
│   │   ├── db/              # Banco de dados e persistência
│   │   ├── llm/             # Clientes OpenAI e Claude
│   │   └── mcp/             # Módulo de consulta persistente (servidor TCP)
│   └── main.py              # Início do sistema de conversação
│
├── scripts/
│   └── populate_db.py       # Popula o banco com dados de teste
│
├── tests/                   # Testes unitários
├── .env                     # Variáveis de ambiente
├── requirements.txt         # Dependências do projeto
└── README.md
```

## ✅ Executando Testes

Este projeto utiliza `pytest` para testes unitários e `pytest-cov` para geração de relatórios de cobertura.

### 🔹 Executar todos os testes

```bash
pytest
```

### 🔹 Executar testes com relatório de cobertura

```bash
pytest --cov=app --cov-report=term
```

Isso exibirá no terminal a cobertura de código (em %) dos módulos principais do projeto.

### 🔹 Gerar relatório de cobertura em HTML (opcional)

```bash
pytest --cov=app --cov-report=html
```

O relatório será salvo na pasta `htmlcov`. Para visualizar:

```bash
start htmlcov/index.html  # Windows
xdg-open htmlcov/index.html  # Linux
open htmlcov/index.html  # macOS
```

## 🛠️ Contribuindo

Contribuições são bem-vindas! Se quiser propor melhorias, abra uma issue ou envie um pull request.

## 📄 Licença

Este projeto está licenciado sob os termos da **MIT License**.
