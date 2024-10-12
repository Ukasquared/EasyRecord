#!/usr/bin/python3
"""student class"""
from models import Base
from models.base import BaseModel
from sqlalchemy import Column, String, DateTime
import uuid
from datetime import datetime
from sqlalchemy.orm import relationship, backref


class Student(Base, BaseModel):
    """student details"""
    __table__ = "student"

    parent = relationship('Parent',backref="student", uselist=False)
    attendance = relationship('Attendance', backref="students")
    student = relationship('Student', backref='course')
    

    def __repr__(self) -> str:
        return f"<Class name: {self.__class__.__name__}>"

    