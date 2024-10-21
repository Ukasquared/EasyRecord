#!/usr/bin/python3
"""parent class"""

from api.models.base import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
# import uuid
# from datetime import datetime


class Parent(BaseModel, Base):
    """parent details"""
    __tablename__ = "parents"
    student_id = Column(String(40), ForeignKey('students.id'), nullable=False)
    admin_id = Column(String(40), ForeignKey('admin.id'), nullable=False)
    student = relationship('Student', back_populates="parent")

    def __repr__(self) -> str:
        return f"<Class name: {self.__class__.__name__}>"

