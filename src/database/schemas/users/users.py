from pydantic import BaseModel

class UserTypeBase(BaseModel):
    name: str
    
class UserType(UserTypeBase):
    id: int
    
    class Config:
        orm_mode=True

class UserBase(BaseModel):
    username: str
    email: str
    
class User(UserBase):
    id: int
    user_type_id: str
    user_type: str
    
    class Config:
        orm_mode: True