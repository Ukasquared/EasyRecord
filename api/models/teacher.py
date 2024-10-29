"""teacher class"""

from api.models.base import BaseModel, Base
from sqlalchemy import Column, Table, ForeignKey, String
from sqlalchemy.orm import relationship
# from ..models.student import Student
# import uuid


class Teacher(BaseModel, Base):
    """teacher details"""
    __tablename__ = "teachers"

    course = relationship("Course", back_populates="teacher", uselist=False)
    admin_id = Column(String(40), ForeignKey('admin.id'), nullable=False)
    student = relationship('Student',  secondary="teacher_student", back_populates="teacher") 
    admin = relationship("Admin", back_populates="teacher")

    def __repr__(self) -> str:
        return f"<Class name: {self.__class__.__name__}>"

teacher_student = Table(
    'teacher_student', 
    Base.metadata,
    Column('teacher_id', String(40), ForeignKey("teachers.id"), primary_key=True),
    Column("student_id", String(40), ForeignKey("students.id"), primary_key=True)
)