#!/usr/bin/python3
"""admin class"""
from models import Base
from models.base import BaseModel
from sqlalchemy.orm import relationship 


class Admin(Base, BaseModel):
    """the admin class
    manages the overall
    activities of the
    school"""
    __table__ = "admin"

    courses = relationship("Course", backref="admin")
    student = relationship("Student", backref="admin")

    def __repr__(self) -> str:
        return f"<Class name: {self.__class__.__name__}>"
