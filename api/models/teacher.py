#!/usr/bin/python3
"""teacher class"""
from models import Base
from sqlalchemy import Column, String, DateTime, Table, ForeignKey
from sqlalchemy.orm import relationship, backref
import uuid
from datetime import datetime


association_table = Table(
    'teacher_student', Base.metadata,
    Column('teacher_id', ForeignKey("teacher.id"), primary_key=True),
    Column("student_id", ForeignKey("student.id"), primary_key=True)
)

class Teacher(Base):
    """teacher details"""
    __table__ = "teacher"

    id = Column(String(100), primary_key=True, default=lambda: str(uuid.uuid4()))
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.now(datetime.timezone.utc))
    gender = Column(String(50), nullable=False)
    religion = Column(String(50), nullable=False)
    student = relationship('Student', backref="teacher")
    course = relationship("Course", backref="teacher")

    
    def __repr__(self) -> str:
        return f"<Class name: {self.__class__.__name__}>"

    