from pydantic import BaseModel

class InserirDados(BaseModel):
    nome: str
    idade: int