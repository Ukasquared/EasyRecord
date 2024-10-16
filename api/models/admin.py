"""admin class"""
from .base import BaseModel, Base
from sqlalchemy.orm import relationship 


class Admin(BaseModel, Base):
    """the admin class
    manages the overall
    activities of the
    school"""
    __tablename__ = "admin"

    course = relationship("Course", back_populates="admin")
    student = relationship("Student", back_populates="admin")
    teacher = relationship("Teacher", back_populates="admin")

    def __repr__(self) -> str:
        return f"<Class name: {self.__class__.__name__}>"