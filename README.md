# Sociedade Científica

## Minimundo

Uma sociedade científica deseja manter um cadastro de pesquisas, contendo o nome da pesquisa, uma breve descrição, data de início, data de término (efetiva e prevista), e a área de pesquisa (entre um conjunto especificado pela sociedade). Cada pesquisa tem um coordenador, sobre o qual é mantido o nome, e-mail, instituição de origem, endereço. Juntamente com as pesquisas pretende-se armazenar informações bibliográficas nas áreas de interesse da sociedade. Sobre as publicações são mantidas as informações usuais (título, ano, autores, ISBN, etc...). No caso de teses mantêm-se o grau a que se refere (Grad - Graduação, Esp - Especialização, MSc – Mestrado em Ciência, DSc – Doutorado em Ciência, PhD – Doutor em Filosofia, etc...) e a instituição onde foi defendida. No caso de livros, armazenam-se a editora (código, nome) e o local de publicação (cidade e UF). No caso de artigos de revistas e conferências, armazenam-se o nome do periódico, volume e número. Cada publicação é associada com áreas de pesquisa correspondentes. A sociedade deseja manter também informações sobre software e tutoriais para o uso em computadores referentes às áreas de pesquisas de interesse da sociedade. Sobre estes, são mantidas o nome, descrição breve, empresa ou pessoa responsável, endereço para contato, equipamento para os quais se encontra disponível, endereço na internet onde pode ser encontrado (quando pertinente), arquivo ou arquivos correspondentes (quando pertinente).

---

## Como rodar

### Pré-requisitos

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) (gerenciador de pacotes)
- MongoDB (local ou Atlas)

### Setup

```bash
# Criar e ativar ambiente virtual (uma vez)
uv venv
.venv\Scripts\activate   # Windows
source .venv/bin/activate # Linux/macOS

# Instalar dependências
uv pip install -r requirements.txt
```

### Backend (FastAPI + MongoDB)

```bash
# Configurar variável de ambiente
# Crie src/backend/.env com:
# MONGODB_URI=mongodb+srv://<user>:<pass>@<cluster>/<db>?retryWrites=true&w=majority

# Iniciar servidor (porta 8000)
python main.py
```

### Frontend (Reflex)

```bash
# Navegar até a pasta do frontend
cd frontend

# Iniciar servidor de desenvolvimento (porta 3000)
reflex run
```

### Acessar

- **Frontend:** http://localhost:3000
- **API:** http://localhost:8000
- **Docs da API:** http://localhost:8000/docs

---

## Estrutura

```
sociedade-cientifica/
├── main.py              # Entrypoint do backend
├── src/backend/api/     # FastAPI + MongoDB
│   ├── app.py
│   ├── routes.py
│   ├── controller/      # Lógica de negócio
│   ├── database/        # Conexão MongoDB
│   └── utils/           # Serialização
├── frontend/            # Reflex app
│   ├── rxconfig.py
│   └── sociedade_front/
│       ├── components/  # Sidebar, breadcrumbs, cards
│       ├── pages/       # Dashboard, Áreas, Pesquisas, etc.
│       └── state/       # Estados Reflex
├── models/              # SQL e NoSQL schemas
└── docs/                # Documentação do modelo
```
