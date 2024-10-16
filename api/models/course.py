
"""courses class"""

from api.models.base import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Table, Integer
from sqlalchemy.orm import relationship
# from datetime import datetime


class Course(BaseModel, Base):
    """all courses"""
    __tablename__ = "courses"
    
    title = Column(String(40), nullable=False)
    teacher_id = Column(String(40), ForeignKey('teachers.id'), nullable=False)
    score = Column(Integer, default=0)
    admin_id = Column(String(40), ForeignKey('admin.id'), nullable=False)
    student = relationship('Student', secondary="courses_student", back_populates='course')
    teacher = relationship("Teacher", back_populates="course")
    admin = relationship("Admin", back_populates="course")

    def __repr__(self) -> str:
        return f"<Class name: {self.__class__.__name__}>"

courses_student = Table(
    'courses_student', 
    Base.metadata,
    Column('course_id', String(40), ForeignKey("courses.id"), primary_key=True),
    Column("student_id", String(40), ForeignKey("students.id"), primary_key=True)
)