from fastapi import APIRouter, HTTPException
from app.database import get_conn
from app.schemas import InserirDados

router = APIRouter()

@router.get("/ping")
async def ping():
    return {"message": "API online"}

@router.post("/inserir")
async def inserir(payload: InserirDados):
    conn = await get_conn()
    try:
        await conn.execute(
            "INSERT INTO teste_api (nome, idade) VALUES ($1, $2)",
            payload.nome, payload.idade
        )
        return {"status": "inserido"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        await conn.close()