from pydantic import BaseModel

class UserCreate(BaseModel):
    login: str
    password: str

class UserResponse(BaseModel):
    id: int
    login: str

    class Config:
        orm_mode = True
