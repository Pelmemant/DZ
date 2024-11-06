from sqlalchemy import  Column, Integer, String, ForeignKey, Boolean
from модуль17.module_17_2.app.backend.db import Base
from sqlalchemy.orm import relationship
from user import User


class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    completed = Column(Boolean, default=False)
    user_id = Column(ForeignKey('users.id'), Integer, index=True ,nullable=False)
    slug = Column(String, unique=True, index=True)
    user = relationship("User", back_populates='tasks')