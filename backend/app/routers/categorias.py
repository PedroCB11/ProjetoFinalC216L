from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/categorias", tags=["categorias"])


@router.get("/", response_model=list[schemas.CategoriaResponse])
def listar_categorias(db: Session = Depends(get_db)):
    return db.query(models.Categoria).order_by(models.Categoria.nome).all()


@router.get("/{categoria_id}", response_model=schemas.CategoriaResponse)
def buscar_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = db.get(models.Categoria, categoria_id)
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria nao encontrada")
    return categoria


@router.post(
    "/",
    response_model=schemas.CategoriaResponse,
    status_code=status.HTTP_201_CREATED,
)
def criar_categoria(
    dados: schemas.CategoriaCreate,
    db: Session = Depends(get_db),
):
    categoria = models.Categoria(**dados.model_dump())
    db.add(categoria)

    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Ja existe uma categoria com esse nome",
        ) from exc

    db.refresh(categoria)
    return categoria


@router.put("/{categoria_id}", response_model=schemas.CategoriaResponse)
def atualizar_categoria(
    categoria_id: int,
    dados: schemas.CategoriaUpdate,
    db: Session = Depends(get_db),
):
    categoria = db.get(models.Categoria, categoria_id)
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria nao encontrada")

    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(categoria, campo, valor)

    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Ja existe uma categoria com esse nome",
        ) from exc

    db.refresh(categoria)
    return categoria


@router.delete("/{categoria_id}", status_code=status.HTTP_204_NO_CONTENT)
def excluir_categoria(categoria_id: int, db: Session = Depends(get_db)):
    categoria = db.get(models.Categoria, categoria_id)
    if categoria is None:
        raise HTTPException(status_code=404, detail="Categoria nao encontrada")

    db.delete(categoria)
    db.commit()
    return None
