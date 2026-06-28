from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session, selectinload

from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/tarefas", tags=["tarefas"])


def buscar_tarefa_ou_erro(tarefa_id: int, db: Session):
    tarefa = (
        db.query(models.Tarefa)
        .options(
            selectinload(models.Tarefa.categoria),
            selectinload(models.Tarefa.tags),
        )
        .filter(models.Tarefa.id == tarefa_id)
        .first()
    )
    if tarefa is None:
        raise HTTPException(status_code=404, detail="Tarefa nao encontrada")
    return tarefa


def validar_categoria(categoria_id: int, db: Session):
    categoria = db.get(models.Categoria, categoria_id)
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria nao encontrada")
    return categoria


@router.get("/", response_model=list[schemas.TarefaResponse])
def listar_tarefas(db: Session = Depends(get_db)):
    return (
        db.query(models.Tarefa)
        .options(
            selectinload(models.Tarefa.categoria),
            selectinload(models.Tarefa.tags),
        )
        .order_by(models.Tarefa.id)
        .all()
    )


@router.get("/{tarefa_id}", response_model=schemas.TarefaResponse)
def buscar_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    return buscar_tarefa_ou_erro(tarefa_id, db)


@router.post("/", response_model=schemas.TarefaResponse, status_code=status.HTTP_201_CREATED)
def criar_tarefa(dados: schemas.TarefaCreate, db: Session = Depends(get_db)):
    validar_categoria(dados.categoria_id, db)

    tarefa = models.Tarefa(**dados.model_dump())
    db.add(tarefa)
    db.commit()
    db.refresh(tarefa)

    return buscar_tarefa_ou_erro(tarefa.id, db)


@router.put("/{tarefa_id}", response_model=schemas.TarefaResponse)
def atualizar_tarefa(
    tarefa_id: int,
    dados: schemas.TarefaUpdate,
    db: Session = Depends(get_db),
):
    tarefa = buscar_tarefa_ou_erro(tarefa_id, db)
    campos = dados.model_dump(exclude_unset=True)

    if "categoria_id" in campos:
        validar_categoria(campos["categoria_id"], db)

    for campo, valor in campos.items():
        setattr(tarefa, campo, valor)

    db.commit()
    db.refresh(tarefa)

    return buscar_tarefa_ou_erro(tarefa.id, db)


@router.delete("/{tarefa_id}", status_code=status.HTTP_204_NO_CONTENT)
def excluir_tarefa(tarefa_id: int, db: Session = Depends(get_db)):
    tarefa = buscar_tarefa_ou_erro(tarefa_id, db)
    db.delete(tarefa)
    db.commit()
    return None
