#!/usr/bin/python3
"""teacher class"""
from models import Base
from models.base import BaseModel
from sqlalchemy import Column, String, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship, backref
import uuid
from datetime import datetime


association_table = Table(
    'teacher_student', Base.metadata,
    Column('teacher_id', ForeignKey("teacher.id"), primary_key=True),
    Column("student_id", ForeignKey("student.id"), primary_key=True)
)

class Teacher(Base, BaseModel):
    """teacher details"""
    __table__ = "teacher"

    student = relationship('Student', backref="teacher")
    course = relationship("Course", backref="teacher")


    def __repr__(self) -> str:
        return f"<Class name: {self.__class__.__name__}>"

    