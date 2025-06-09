import asyncpg
import os
from dotenv import load_dotenv

load_dotenv()

async def get_conn():
    return await asyncpg.connect(os.getenv("DATABASE_URL"))