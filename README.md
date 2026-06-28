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
├── backend/
│   └── app/
├── database/
├── docs/
├── frontend/
│   ├── static/
│   └── templates/
├── docker-compose.yml
└── README.md
```

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
