# Gerenciador de Tarefas de Estudos

Projeto final da disciplina C216. A proposta e construir uma aplicacao web simples para organizar tarefas de estudo por categorias e tags.

## Tema

O sistema permite cadastrar tarefas de estudo, organizar cada tarefa em uma categoria e associar tags para facilitar filtros e acompanhamento.

## Tecnologias planejadas

- Backend: FastAPI
- Testes: Pytest
- Frontend: Flask
- Banco de dados: PostgreSQL
- Orquestracao: Docker Compose

## Estrutura inicial

```text
.
|-- backend/
|   |-- app/
|   |   |-- database.py
|   |   |-- main.py
|   |   `-- models.py
|   |-- Dockerfile
|   `-- requirements.txt
|-- database/
|   `-- schema.sql
|-- docs/
|-- frontend/
|   |-- static/
|   |-- templates/
|   |-- Dockerfile
|   |-- app.py
|   `-- requirements.txt
|-- docker-compose.yml
`-- README.md
```

## Modelo do banco

Tabelas iniciais:

- `categorias`: categorias das tarefas de estudo.
- `tarefas`: tarefas cadastradas pelo usuario.
- `tags`: marcadores reutilizaveis para classificar tarefas.
- `tarefa_tags`: tabela associativa da relacao N:M entre tarefas e tags.

Relacoes:

- Uma categoria possui varias tarefas (`1:N`).
- Uma tarefa pode possuir varias tags e uma tag pode estar em varias tarefas (`N:M`).

## Rotas implementadas

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

## Como executar

Com Docker instalado, execute:

```bash
docker compose up --build
```

Servicos planejados:

- Frontend: http://localhost:5000
- Backend: http://localhost:8000
- Documentacao da API: http://localhost:8000/docs
- PostgreSQL: localhost:5432

## Requisitos do projeto

- Frontend com pelo menos 3 telas
- Backend com rotas REST usando GET, POST, PUT e DELETE
- Pelo menos 10 operacoes no backend
- Banco com relacao 1:N e N:M
- Testes do backend
- Aplicacao executando por Docker Compose
- README com instrucoes e boas praticas de uso
