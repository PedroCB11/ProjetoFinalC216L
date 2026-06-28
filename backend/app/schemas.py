from pydantic import BaseModel, ConfigDict


class CategoriaBase(BaseModel):
    nome: str
    descricao: str | None = None


class CategoriaCreate(CategoriaBase):
    pass


class CategoriaUpdate(BaseModel):
    nome: str | None = None
    descricao: str | None = None


class CategoriaResponse(CategoriaBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


class TagBase(BaseModel):
    nome: str


class TagCreate(TagBase):
    pass


class TagUpdate(BaseModel):
    nome: str | None = None


class TagResponse(TagBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
