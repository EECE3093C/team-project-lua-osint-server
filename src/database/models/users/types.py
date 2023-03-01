from sqlalchemy import Boolean, Column, Integer, String 
from ..base import Base

class UserType(Base):
    __tablename__ = 'user_types'
    
    id=Column(Integer, primary_key=True, index=True)
    name=Column(String(50), unique=True, index=True)
