#!/usr/bin/python3
"""parent class"""
from models import Base
from models.base import BaseModel
from sqlalchemy import Column, String, DateTime, ForeignKey
import uuid
from datetime import datetime


class Parent(Base, BaseModel):
    """parent details"""
    __table__ = "parent"
    student_id = Column(String(40), ForeignKey('student.id'))



    def __repr__(self) -> str:
        return f"<Class name: {self.__class__.__name__}>"

