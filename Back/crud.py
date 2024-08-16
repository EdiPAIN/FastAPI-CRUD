from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from Back.models import User
from Back.schemas import UserCreate

async def create_user(session: AsyncSession, user: UserCreate) -> User:
    new_user = User(login=user.login, password=user.password)
    session.add(new_user)
    await session.commit()
    await session.refresh(new_user)
    return new_user

async def get_user_by_id(session: AsyncSession, user_id: int) -> User:
    return await session.get(User, user_id)

async def get_all_users(session: AsyncSession):
    result = await session.execute(select(User))
    return result.scalars().all()

async def update_user(session: AsyncSession, user_id: int, user_data: UserCreate):
    user = await session.get(User, user_id)
    if user:
        user.login = user_data.login
        user.password = user_data.password
        await session.commit()
        await session.refresh(user)
    return user

async def delete_user(session: AsyncSession, user_id: int):
    user = await session.get(User, user_id)
    if user:
        await session.delete(user)
        await session.commit()
    return user
