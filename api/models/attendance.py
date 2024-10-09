#!/usr/bin/python3
"""attendance class"""
from models import Base
from sqlalchemy import Column, String, DateTime, ForeignKey, Boolean
import uuid
# from datetime import datetime


class Attendance(Base):
    """Attendance of
    students"""
    __table__ = "attendance"

    id = Column(String(40), primary_key=True, default=lambda: str(uuid.uuid4()))
    student_id = Column(String(40), ForeignKey('student.id'))
    date = Column(DateTime)
    status = Column(Boolean, default=False)

    def __repr__(self) -> str:
        return f"<Class name: {self.__class__.__name__}>"
