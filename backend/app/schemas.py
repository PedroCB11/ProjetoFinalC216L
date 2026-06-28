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


class TarefaBase(BaseModel):
    titulo: str
    descricao: str | None = None
    concluida: bool = False
    categoria_id: int


class TarefaCreate(TarefaBase):
    pass


class TarefaUpdate(BaseModel):
    titulo: str | None = None
    descricao: str | None = None
    concluida: bool | None = None
    categoria_id: int | None = None


class TarefaResponse(TarefaBase):
    id: int
    categoria: CategoriaResponse
    tags: list[TagResponse] = []

    model_config = ConfigDict(from_attributes=True)
