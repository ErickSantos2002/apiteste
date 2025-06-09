from fastapi import FastAPI
from app.routes import dados

app = FastAPI()
app.include_router(dados.router)
