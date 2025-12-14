from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    password: str
    
class UserRead(BaseModel):
    id: int
    username: str
    class Config:
        orm_mode = True

class Token(BaseModel):
    access_token: str
    token_type: str
    
class RollType(BaseModel):
    number: int
    
class CardRead(BaseModel):
    id: int
    name: str
    class Config:
        orm_mode = True