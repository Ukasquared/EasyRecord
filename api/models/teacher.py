#!/usr/bin/python3
"""teacher class"""
from models import Base
from models.base import BaseModel
from sqlalchemy import Column, Table, ForeignKey, String
from sqlalchemy.orm import relationship, backref
# import uuid


association_table = Table(
    'teacher_student', Base.metadata,
    Column('teacher_id', ForeignKey("teacher.id"), primary_key=True),
    Column("student_id", ForeignKey("student.id"), primary_key=True)
)

class Teacher(Base, BaseModel):
    """teacher details"""
    __table__ = "teacher"

    student = relationship('Student', backref="teacher")
    course = relationship("Course", backref="teacher", uselist=False)
    admin_id = Column(String(40), ForeignKey('admin.id'), nullable=False)


    def __repr__(self) -> str:
        return f"<Class name: {self.__class__.__name__}>"
