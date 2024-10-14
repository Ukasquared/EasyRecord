#!/usr/bin/python3
"""courses class"""
from models import Base
from models.base import BaseModel
from sqlalchemy import Column, String, ForeignKey, Table, Integer
# from sqlalchemy.orm import relationship, backref
# from datetime import datetime


association_table = Table(
    'courses_student', Base.metadata,
    Column('course_id', ForeignKey("course.id"), primary_key=True),
    Column("student_id", ForeignKey("student.id"), primary_key=True)
)

class Course(Base, BaseModel):
    """all courses"""
    __table__ = "course"
    
    title = Column(String(40), nullable=False)
    teacher_id = Column(String(40), ForeignKey('teacher.id'), nullable=False)
    score = Column(Integer, default=0)
    admin_id = Column(String(40), ForeignKey('admin.id'), nullable=False)


    def __repr__(self) -> str:
        return f"<Class name: {self.__class__.__name__}>"
    