
"""courses class"""

from api.models.base import Base
from sqlalchemy import Column, String, ForeignKey, Table, Integer, Date
from sqlalchemy.orm import relationship
import uuid
from datetime import date
# from datetime import datetime


class Course(Base):
    """all courses"""
    __tablename__ = "courses"
    
    id = Column(String(40), primary_key=True, nullable=False)
    title = Column(String(40), nullable=False)
    teacher_id = Column(String(40), ForeignKey('teachers.id'), nullable=False)
    score = Column(Integer, default=0)
    admin_id = Column(String(40), ForeignKey('admin.id'), nullable=False)
    student = relationship('Student', secondary="courses_student", back_populates='course')
    teacher = relationship("Teacher", back_populates="course")
    admin = relationship("Admin", back_populates="course")
    created_at = Column(Date)
    updated_at = Column(Date)

    def __init__(self, **kwargs) -> None:
        """creates an instance
        of the class"""
        if kwargs:
            for k, v in kwargs.items():
                setattr(self, k, v)
        self.id = str(uuid.uuid4())
        self.created_at = date.today()
        self.updated_at = date.today()

    def __repr__(self) -> str:
        return f"<Class name: {self.__class__.__name__}>"
    
    def new(self)-> None:
        """Create a new object."""
        from api.models import storage
        storage.add_user(self)
        storage.save()

courses_student = Table(
    'courses_student', 
    Base.metadata,
    Column('course_id', String(40), ForeignKey("courses.id"), primary_key=True),
    Column("student_id", String(40), ForeignKey("students.id"), primary_key=True)
)