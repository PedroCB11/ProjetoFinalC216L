CREATE TABLE IF NOT EXISTS categorias (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(80) UNIQUE NOT NULL,
    descricao TEXT
);

CREATE TABLE IF NOT EXISTS tarefas (
    id SERIAL PRIMARY KEY,
    titulo VARCHAR(120) NOT NULL,
    descricao TEXT,
    concluida BOOLEAN NOT NULL DEFAULT FALSE,
    categoria_id INTEGER NOT NULL REFERENCES categorias(id)
);

CREATE TABLE IF NOT EXISTS tags (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(60) UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS tarefa_tags (
    tarefa_id INTEGER NOT NULL REFERENCES tarefas(id),
    tag_id INTEGER NOT NULL REFERENCES tags(id),
    PRIMARY KEY (tarefa_id, tag_id)
);
