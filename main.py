from fastapi import FastAPI
from sqlalchemy import text
from database import async_session

app = FastAPI()

@app.get("/")
async def read_root():
    async with async_session() as session:
        query = text("SELECT * FROM public.users")
        result = await session.execute(query)
        rows = result.mappings().all()
        return {"result": rows}
