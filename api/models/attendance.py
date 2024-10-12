#!/usr/bin/python3
"""attendance class"""
from models import Base
from models.base import BaseModel
from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean
import uuid
# from datetime import datetime


class Attendance(Base, BaseModel):
    """Attendance of
    students"""
    __table__ = "attendance"

    student_id = Column(String(40), ForeignKey('student.id'))
    date = Column(DateTime)
    status = Column(Boolean, default=False)

    def __repr__(self) -> str:
        return f"<Class name: {self.__class__.__name__}>"
