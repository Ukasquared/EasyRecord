#!/usr/bin/python3
"""student class"""
from models import Base
from sqlalchemy import Column, String, DateTime
import uuid
from datetime import datetime
from sqlalchemy.orm import relationship, backref


class Student(Base):
    """student details"""
    __table__ = "student"

    id = Column(String(100), primary_key=True, default=lambda: str(uuid.uuid4()))
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.now(datetime.timezone.utc))
    gender = Column(String(50), nullable=False)
    religion = Column(String(50), nullable=False)
    parent = relationship('Parent',backref="student", uselist=False)
    attendance = relationship('Attendance', backref="students")
    student = relationship('Student', backref='course')
    

    def __repr__(self) -> str:
        return f"<Class name: {self.__class__.__name__}>"

    