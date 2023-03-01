from sqlalchemy import Boolean, Column, ForeignKey, Integer, String 
from sqlalchemy.orm import relationship

from ..base import Base
from .types import UserType

class User(Base):
    __tablename__ = 'users'
    
    id=Column(Integer, primary_key=True, index=True)
    username=Column(String, unique=True, index=True)
    email=Column(String, unique=True, index=True)
    hashed_password=Column(String)
    
    user_type_id=Column(Integer, ForeignKey("user_type.id"), default=1)
    user_type=relationship(UserType, back_populates=True)
