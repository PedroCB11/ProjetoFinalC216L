import os

os.environ["DATABASE_URL"] = "sqlite+pysqlite:///:memory:"

from fastapi.testclient import TestClient

from app.database import Base, engine
from app.main import app


client = TestClient(app)


def setup_function():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)


def criar_categoria(nome="Matematica"):
    response = client.post(
        "/categorias/",
        json={"nome": nome, "descricao": "Conteudos para revisar"},
    )
    assert response.status_code == 201
    return response.json()


def criar_tag(nome="prova"):
    response = client.post("/tags/", json={"nome": nome})
    assert response.status_code == 201
    return response.json()


def criar_tarefa(categoria_id, titulo="Revisar listas"):
    response = client.post(
        "/tarefas/",
        json={
            "titulo": titulo,
            "descricao": "Resolver exercicios antes da avaliacao",
            "concluida": False,
            "categoria_id": categoria_id,
        },
    )
    assert response.status_code == 201
    return response.json()


def test_cria_lista_atualiza_e_remove_categoria():
    categoria = criar_categoria()

    listagem = client.get("/categorias/")
    assert listagem.status_code == 200
    assert listagem.json()[0]["nome"] == "Matematica"

    atualizada = client.put(
        f"/categorias/{categoria['id']}",
        json={"nome": "Fisica", "descricao": "Exercicios de revisao"},
    )
    assert atualizada.status_code == 200
    assert atualizada.json()["nome"] == "Fisica"

    removida = client.delete(f"/categorias/{categoria['id']}")
    assert removida.status_code == 204

    inexistente = client.get(f"/categorias/{categoria['id']}")
    assert inexistente.status_code == 404


def test_cria_lista_atualiza_e_remove_tag():
    tag = criar_tag()

    listagem = client.get("/tags/")
    assert listagem.status_code == 200
    assert listagem.json()[0]["nome"] == "prova"

    atualizada = client.put(f"/tags/{tag['id']}", json={"nome": "urgente"})
    assert atualizada.status_code == 200
    assert atualizada.json()["nome"] == "urgente"

    removida = client.delete(f"/tags/{tag['id']}")
    assert removida.status_code == 204

    inexistente = client.get(f"/tags/{tag['id']}")
    assert inexistente.status_code == 404


def test_cria_lista_atualiza_e_remove_tarefa():
    categoria = criar_categoria()
    tarefa = criar_tarefa(categoria["id"])

    listagem = client.get("/tarefas/")
    assert listagem.status_code == 200
    assert listagem.json()[0]["titulo"] == "Revisar listas"
    assert listagem.json()[0]["categoria"]["nome"] == "Matematica"

    atualizada = client.put(
        f"/tarefas/{tarefa['id']}",
        json={"titulo": "Revisar capitulos", "concluida": True},
    )
    assert atualizada.status_code == 200
    assert atualizada.json()["titulo"] == "Revisar capitulos"
    assert atualizada.json()["concluida"] is True

    removida = client.delete(f"/tarefas/{tarefa['id']}")
    assert removida.status_code == 204

    inexistente = client.get(f"/tarefas/{tarefa['id']}")
    assert inexistente.status_code == 404


def test_adiciona_e_remove_tag_da_tarefa():
    categoria = criar_categoria()
    tag = criar_tag()
    tarefa = criar_tarefa(categoria["id"])

    associada = client.post(f"/tarefas/{tarefa['id']}/tags/{tag['id']}")
    assert associada.status_code == 200
    assert associada.json()["tags"][0]["nome"] == "prova"

    removida = client.delete(f"/tarefas/{tarefa['id']}/tags/{tag['id']}")
    assert removida.status_code == 200
    assert removida.json()["tags"] == []


def test_nao_cria_tarefa_com_categoria_inexistente():
    response = client.post(
        "/tarefas/",
        json={
            "titulo": "Ler resumo",
            "descricao": None,
            "concluida": False,
            "categoria_id": 999,
        },
    )

    assert response.status_code == 404
    assert response.json()["detail"] == "Categoria nao encontrada"
