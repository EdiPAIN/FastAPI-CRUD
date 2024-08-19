from fastapi import FastAPI
from Back.models import Base
from Back.database import engine

app = FastAPI()

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

@app.on_event("startup")
async def startup_event():
    await init_db()
