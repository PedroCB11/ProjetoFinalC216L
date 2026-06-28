from fastapi import FastAPI

app = FastAPI(title="Gerenciador de Tarefas de Estudos")


@app.get("/")
def root():
    return {"message": "API do Gerenciador de Tarefas de Estudos"}


@app.get("/health")
def health_check():
    return {"status": "ok"}
