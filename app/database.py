import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()

async def get_conn():
    conn = await asyncpg.connect(os.getenv("DATABASE_URL"))
    await conn.execute('SET search_path TO public')
    return conn