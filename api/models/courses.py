#!/usr/bin/python3
"""courses class"""
from models import Base
from sqlalchemy import Column, String, ForeignKey, Table, Integer
# from sqlalchemy.orm import relationship, backref
import uuid
# from datetime import datetime


association_table = Table(
    'courses_student', Base.metadata,
    Column('course_id', ForeignKey("courses.id"), primary_key=True),
    Column("student_id", ForeignKey("student.id"), primary_key=True)
)

class Course(Base):
    """all courses"""
    __table__ = "courses"
    id = Column(String(40), primary_key=True, default= lambda: uuid.uuid4())
    title = Column(String(40), nullable=False)
    teacher_id = Column(String(40), ForeignKey('teacher.id'))
    score = Column(Integer, default=0)


   



    def __repr__(self) -> str:
        return f"<Class name: {self.__class__.__name__}>"



