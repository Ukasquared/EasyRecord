#!/usr/bin/python3
"""admin class"""
from models import Base
from sqlalchemy import Column, Integer, String, DateTime
import uuid
from datetime import datetime


class Admin(Base):
    """the admin class
    manages the overall
    activities of the
    school"""
    __table__ = "admin"

    id = Column(String(100), primary_key=True, default=lambda: str(uuid.uuid4()))
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    username = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=datetime.now(datetime.timezone.utc))
    gender = Column(String(50), nullable=False)
    religion = Column(String(50), nullable=False)


    def __repr__(self) -> str:
        return f"<Class name: {self.__class__.__name__}>"
