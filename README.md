# Gerenciador de Tarefas de Estudos

Projeto final da disciplina C216. A aplicacao organiza tarefas de estudo por categorias e tags, com backend REST, frontend web, persistencia em PostgreSQL e execucao via Docker Compose.

## Funcionalidades

- Cadastro, listagem, conclusao e exclusao de tarefas.
- Cadastro, listagem e exclusao de categorias.
- Cadastro, listagem e exclusao de tags.
- Associacao e remocao de tags em tarefas.
- Consulta das tarefas com categoria e tags vinculadas.

## Tecnologias

- Backend: FastAPI
- ORM: SQLAlchemy
- Banco de dados: PostgreSQL
- Frontend: Flask + HTML + CSS
- Testes: Pytest
- Containers: Docker e Docker Compose

## Como executar com Docker

Com o Docker Desktop aberto, execute na raiz do projeto:

```bash
docker compose up --build
```

Servicos:

- Frontend: http://localhost:5000
- Backend: http://localhost:8000
- Documentacao da API: http://localhost:8000/docs
- PostgreSQL: localhost:5432

Para acompanhar os logs:

```bash
docker compose logs -f
```

Para parar os containers:

```bash
docker compose down
```

Se o Docker Desktop retornar erro de conexao com o engine ou erro 500, reinicie o Docker Desktop e execute o comando novamente. Os arquivos `.dockerignore` removem caches Python do contexto de build para evitar falhas com `__pycache__` no Windows/OneDrive.

## Telas do frontend

- `/tarefas`: cadastro, listagem, conclusao, exclusao e associacao de tags em tarefas.
- `/categorias`: cadastro, listagem e exclusao de categorias.
- `/tags`: cadastro, listagem e exclusao de tags.

## Rotas da API

Categorias:

- `GET /categorias/`
- `GET /categorias/{categoria_id}`
- `POST /categorias/`
- `PUT /categorias/{categoria_id}`
- `DELETE /categorias/{categoria_id}`

Tags:

- `GET /tags/`
- `GET /tags/{tag_id}`
- `POST /tags/`
- `PUT /tags/{tag_id}`
- `DELETE /tags/{tag_id}`

Tarefas:

- `GET /tarefas/`
- `GET /tarefas/{tarefa_id}`
- `POST /tarefas/`
- `PUT /tarefas/{tarefa_id}`
- `DELETE /tarefas/{tarefa_id}`
- `POST /tarefas/{tarefa_id}/tags/{tag_id}`
- `DELETE /tarefas/{tarefa_id}/tags/{tag_id}`

## Modelo do banco

Tabelas:

- `categorias`: categorias das tarefas de estudo.
- `tarefas`: tarefas cadastradas pelo usuario.
- `tags`: marcadores reutilizaveis.
- `tarefa_tags`: tabela associativa entre tarefas e tags.

Relacoes:

- `categorias` para `tarefas`: relacao `1:N`.
- `tarefas` para `tags`: relacao `N:M` por meio de `tarefa_tags`.

## Estrutura do projeto

```text
.
|-- backend/
|   |-- app/
|   |   |-- routers/
|   |   |-- database.py
|   |   |-- main.py
|   |   |-- models.py
|   |   `-- schemas.py
|   |-- tests/
|   |-- .dockerignore
|   |-- Dockerfile
|   `-- requirements.txt
|-- database/
|   `-- schema.sql
|-- docs/
|-- frontend/
|   |-- static/
|   |-- templates/
|   |-- .dockerignore
|   |-- Dockerfile
|   |-- app.py
|   `-- requirements.txt
|-- docker-compose.yml
|-- pytest.ini
`-- README.md
```

## Como executar os testes

Execute na raiz do projeto:

```bash
pytest
```

Os testes usam SQLite em memoria para validar as rotas principais do backend sem depender do PostgreSQL local.

## Exemplos de uso da API

Criar categoria:

```bash
curl -X POST http://localhost:8000/categorias/ -H "Content-Type: application/json" -d "{\"nome\":\"Matematica\",\"descricao\":\"Listas e revisoes\"}"
```

Criar tag:

```bash
curl -X POST http://localhost:8000/tags/ -H "Content-Type: application/json" -d "{\"nome\":\"prova\"}"
```

Criar tarefa:

```bash
curl -X POST http://localhost:8000/tarefas/ -H "Content-Type: application/json" -d "{\"titulo\":\"Revisar funcoes\",\"descricao\":\"Resolver exercicios\",\"concluida\":false,\"categoria_id\":1}"
```

Associar tag em tarefa:

```bash
curl -X POST http://localhost:8000/tarefas/1/tags/1
```

## Boas praticas de uso

- Cadastre categorias antes de criar tarefas.
- Cadastre tags antes de associa-las a tarefas.
- Use a documentacao em `/docs` para testar as rotas do backend.
- Acompanhe `docker compose logs -f` durante a demonstracao para mostrar os logs dos servicos.
- Pare os containers com `docker compose down` ao finalizar.

## Roteiro sugerido para o video

1. Apresentar a ideia do Gerenciador de Tarefas de Estudos.
2. Mostrar o projeto rodando com `docker compose up --build`.
3. Abrir o frontend em `http://localhost:5000`.
4. Demonstrar as telas de tarefas, categorias e tags.
5. Abrir `http://localhost:8000/docs` e mostrar as rotas REST.
6. Mostrar o modelo do banco em `database/schema.sql`.
7. Exibir os logs com `docker compose logs -f`.
8. Rodar ou mostrar o resultado de `pytest`.

## Atendimento aos requisitos

- Frontend com pelo menos 3 telas: tarefas, categorias e tags.
- Backend REST com `GET`, `POST`, `PUT` e `DELETE`.
- Mais de 10 operacoes no backend.
- Banco com mais de 2 tabelas.
- Relacao `1:N`: categorias e tarefas.
- Relacao `N:M`: tarefas e tags.
- Testes automatizados com Pytest.
- Execucao via Docker Compose.