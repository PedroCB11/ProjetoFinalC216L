import os

import requests
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

API_BASE_URL = os.getenv("API_BASE_URL", "http://localhost:8000")
API_TIMEOUT = 1.5


def api_get(path, default=None):
    try:
        response = requests.get(f"{API_BASE_URL}{path}", timeout=API_TIMEOUT)
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return default if default is not None else []


def api_send(method, path, payload=None):
    try:
        response = requests.request(
            method,
            f"{API_BASE_URL}{path}",
            json=payload,
            timeout=API_TIMEOUT,
        )
        return response.ok
    except requests.RequestException:
        return False


@app.get("/")
def index():
    return redirect(url_for("tarefas"))


@app.get("/tarefas")
def tarefas():
    return render_template(
        "tarefas.html",
        tarefas=api_get("/tarefas/", []),
        categorias=api_get("/categorias/", []),
        tags=api_get("/tags/", []),
    )


@app.post("/tarefas")
def criar_tarefa():
    payload = {
        "titulo": request.form["titulo"],
        "descricao": request.form.get("descricao") or None,
        "concluida": False,
        "categoria_id": int(request.form["categoria_id"]),
    }
    api_send("POST", "/tarefas/", payload)
    return redirect(url_for("tarefas"))


@app.post("/tarefas/<int:tarefa_id>/concluir")
def concluir_tarefa(tarefa_id):
    api_send("PUT", f"/tarefas/{tarefa_id}", {"concluida": True})
    return redirect(url_for("tarefas"))


@app.post("/tarefas/<int:tarefa_id>/excluir")
def excluir_tarefa(tarefa_id):
    api_send("DELETE", f"/tarefas/{tarefa_id}")
    return redirect(url_for("tarefas"))


@app.post("/tarefas/<int:tarefa_id>/tags")
def vincular_tag(tarefa_id):
    tag_id = int(request.form["tag_id"])
    api_send("POST", f"/tarefas/{tarefa_id}/tags/{tag_id}")
    return redirect(url_for("tarefas"))


@app.post("/tarefas/<int:tarefa_id>/tags/<int:tag_id>/remover")
def remover_tag(tarefa_id, tag_id):
    api_send("DELETE", f"/tarefas/{tarefa_id}/tags/{tag_id}")
    return redirect(url_for("tarefas"))


@app.get("/categorias")
def categorias():
    return render_template("categorias.html", categorias=api_get("/categorias/", []))


@app.post("/categorias")
def criar_categoria():
    payload = {
        "nome": request.form["nome"],
        "descricao": request.form.get("descricao") or None,
    }
    api_send("POST", "/categorias/", payload)
    return redirect(url_for("categorias"))


@app.post("/categorias/<int:categoria_id>/excluir")
def excluir_categoria(categoria_id):
    api_send("DELETE", f"/categorias/{categoria_id}")
    return redirect(url_for("categorias"))


@app.get("/tags")
def tags():
    return render_template("tags.html", tags=api_get("/tags/", []))


@app.post("/tags")
def criar_tag():
    api_send("POST", "/tags/", {"nome": request.form["nome"]})
    return redirect(url_for("tags"))


@app.post("/tags/<int:tag_id>/excluir")
def excluir_tag(tag_id):
    api_send("DELETE", f"/tags/{tag_id}")
    return redirect(url_for("tags"))
