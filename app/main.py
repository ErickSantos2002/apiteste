from fastapi import FastAPI
from routes import dados

app = FastAPI()
app.include_router(dados.router)
