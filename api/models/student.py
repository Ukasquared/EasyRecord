#!/usr/bin/python3
"""student class"""
from api.models.base import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
# from datetime import datetime
from sqlalchemy.orm import relationship


class Student(BaseModel, Base):
    """student details"""
    __tablename__ = "students"

    parent = relationship('Parent', back_populates="student", uselist=False)
    # attendance = relationship('Attendance', backref="students")
    course = relationship('Course', secondary="courses_student", back_populates='student')
    admin_id = Column(String(40), ForeignKey('admin.id'), nullable=False)
    teacher = relationship('Teacher',  secondary="teacher_student",  back_populates="student")
    admin = relationship("Admin", back_populates="student")

    def __repr__(self) -> str:
        return f"<Class name: {self.__class__.__name__}>"
