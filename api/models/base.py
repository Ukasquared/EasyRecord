#!/usr/bin/python3
"""base model"""
from sqlalchemy import Column, String, Date
import uuid
from datetime import date


#create user, save user, delete user


class BaseModel:
    """base_model
    of all classes"""
    id = Column(String(40), primary_key=True)
    firstname = Column(String(50), nullable=False)
    lastname = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    gender = Column(String(50), nullable=False)
    photo = Column(String(50), nullable=False)
    role = Column(String(50), nullable=False)
    religion = Column(String(50), nullable=False)
    created_at = Column(Date)
    updated_at = Column(Date)
    password = Column(String(50), nullable=False)
    reset_token = Column(String(40), nullable=True)
    session_id = Column(String(40), nullable=True)


    def __init__(self) -> None:
        """creates an instance
        of the class"""
        self.id = str(uuid.uuid4())
        self.created_at = date.today()
        self.updated_at = date.today()

    def new(self)-> None:
        """create a
        new object"""
        from models import storage
        storage.add_user(self)
        storage.save()

    def update_user_info(self, *kwargs):
        """update the user data
        in the database"""
        from models import storage
        user = storage.find_user(self, self.id)
        for k, v in kwargs.items:
            if hasattr(user, k):
                setattr(user, k, v)
        storage.save()
