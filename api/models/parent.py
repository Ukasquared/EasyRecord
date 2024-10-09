#!/usr/bin/python3
"""parent class"""
from models import Base
from sqlalchemy import Column, String, DateTime, ForeignKey
import uuid
from datetime import datetime


class Parent(Base):
    """parent details"""
    __table__ = "parent"

    id = Column(String(100), primary_key=True, default=lambda: str(uuid.uuid4()))
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.now(datetime.timezone.utc))
    gender = Column(String(50), nullable=False)
    religion = Column(String(50), nullable=False)
    student_id = Column(String(40), ForeignKey('student.id'))

    

    def __repr__(self) -> str:
        return f"<Class name: {self.__class__.__name__}>"

