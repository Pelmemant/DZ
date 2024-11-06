from sqlalchemy import  Column, Integer, String, ForeignKey, Boolean
from module17.module_17_2.app.backend.db import Base
from sqlalchemy.orm import relationship
from module17.module_17_3.app.models import *

class User(Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    firstname = Column(String)
    lastname = Column(String)
    age = Column(Integer)
    slug = Column(String, unique=True, index=True)
    tasks = relationship("Task", back_populates='user')
