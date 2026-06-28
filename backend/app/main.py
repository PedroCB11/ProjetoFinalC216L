from fastapi import Depends, FastAPI
from sqlalchemy import text
from sqlalchemy.orm import Session

from app import models
from app.database import Base, engine, get_db
from app.routers import categorias, tags, tarefas

app = FastAPI(title="Gerenciador de Tarefas de Estudos")
app.include_router(categorias.router)
app.include_router(tags.router)
app.include_router(tarefas.router)


@app.on_event("startup")
def create_tables():
    Base.metadata.create_all(bind=engine)


@app.get("/")
def root():
    return {"message": "API do Gerenciador de Tarefas de Estudos"}


@app.get("/health")
def health_check(db: Session = Depends(get_db)):
    db.execute(text("SELECT 1"))
    return {"status": "ok", "database": "connected"}
