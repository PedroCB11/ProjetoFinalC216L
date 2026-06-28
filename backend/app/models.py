from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Table, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

tarefa_tags = Table(
    "tarefa_tags",
    Base.metadata,
    Column("tarefa_id", Integer, ForeignKey("tarefas.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True),
)


class Categoria(Base):
    __tablename__ = "categorias"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(String(80), unique=True, index=True)
    descricao: Mapped[str | None] = mapped_column(Text, nullable=True)

    tarefas: Mapped[list["Tarefa"]] = relationship(
        back_populates="categoria",
        cascade="all, delete-orphan",
    )


class Tarefa(Base):
    __tablename__ = "tarefas"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    titulo: Mapped[str] = mapped_column(String(120), index=True)
    descricao: Mapped[str | None] = mapped_column(Text, nullable=True)
    concluida: Mapped[bool] = mapped_column(Boolean, default=False)
    categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias.id"))

    categoria: Mapped[Categoria] = relationship(back_populates="tarefas")
    tags: Mapped[list["Tag"]] = relationship(
        secondary=tarefa_tags,
        back_populates="tarefas",
    )


class Tag(Base):
    __tablename__ = "tags"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nome: Mapped[str] = mapped_column(String(60), unique=True, index=True)

    tarefas: Mapped[list[Tarefa]] = relationship(
        secondary=tarefa_tags,
        back_populates="tags",
    )
