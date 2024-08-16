from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from Back.database import get_session
from Back.crud import create_user, get_user_by_id, get_all_users, update_user, delete_user
from Back.schemas import UserCreate, UserResponse

app = FastAPI()

@app.post("/users/post/", response_model=UserResponse)
async def create_new_user(user: UserCreate, session: AsyncSession = Depends(get_session)):
    return await create_user(session, user)

@app.get("/users/get/{user_id}", response_model=UserResponse)
async def read_user(user_id: int, session: AsyncSession = Depends(get_session)):
    user = await get_user_by_id(session, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@app.get("/users/", response_model=list[UserResponse])
async def read_users(session: AsyncSession = Depends(get_session)):
    return await get_all_users(session)

@app.put("/users/put/{user_id}", response_model=UserResponse)
async def update_existing_user(user_id: int, user: UserCreate, session: AsyncSession = Depends(get_session)):
    updated_user = await update_user(session, user_id, user)
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@app.delete("/users/del/{user_id}")
async def delete_existing_user(user_id: int, session: AsyncSession = Depends(get_session)):
    deleted_user = await delete_user(session, user_id)
    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"ok": True}
