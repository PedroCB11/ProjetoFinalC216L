from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from app import models, schemas
from app.database import get_db

router = APIRouter(prefix="/tags", tags=["tags"])


@router.get("/", response_model=list[schemas.TagResponse])
def listar_tags(db: Session = Depends(get_db)):
    return db.query(models.Tag).order_by(models.Tag.nome).all()


@router.get("/{tag_id}", response_model=schemas.TagResponse)
def buscar_tag(tag_id: int, db: Session = Depends(get_db)):
    tag = db.get(models.Tag, tag_id)
    if tag is None:
        raise HTTPException(status_code=404, detail="Tag nao encontrada")
    return tag


@router.post("/", response_model=schemas.TagResponse, status_code=status.HTTP_201_CREATED)
def criar_tag(dados: schemas.TagCreate, db: Session = Depends(get_db)):
    tag = models.Tag(**dados.model_dump())
    db.add(tag)

    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Ja existe uma tag com esse nome",
        ) from exc

    db.refresh(tag)
    return tag


@router.put("/{tag_id}", response_model=schemas.TagResponse)
def atualizar_tag(
    tag_id: int,
    dados: schemas.TagUpdate,
    db: Session = Depends(get_db),
):
    tag = db.get(models.Tag, tag_id)
    if tag is None:
        raise HTTPException(status_code=404, detail="Tag nao encontrada")

    for campo, valor in dados.model_dump(exclude_unset=True).items():
        setattr(tag, campo, valor)

    try:
        db.commit()
    except IntegrityError as exc:
        db.rollback()
        raise HTTPException(
            status_code=409,
            detail="Ja existe uma tag com esse nome",
        ) from exc

    db.refresh(tag)
    return tag


@router.delete("/{tag_id}", status_code=status.HTTP_204_NO_CONTENT)
def excluir_tag(tag_id: int, db: Session = Depends(get_db)):
    tag = db.get(models.Tag, tag_id)
    if tag is None:
        raise HTTPException(status_code=404, detail="Tag nao encontrada")

    db.delete(tag)
    db.commit()
    return None
