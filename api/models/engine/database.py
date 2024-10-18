#!/usr/bin/python3
"""database class"""
from api.models.base import Base
from api.models.admin import Admin
from api.models.student import Student
from api.models.course import Course
from api.models.parent import Parent
from api.models.teacher import Teacher
from sqlalchemy.orm import sessionmaker, scoped_session
# from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy import create_engine


class Database:
    """store users
    info into database
    """
    _engine = None
    _session = None

    def __init__(self) -> None:
        """initialize an instance
        and creates a connection 
        to database"""
    
        self._engine = create_engine(
            'mysql+mysqldb://root:root@localhost/easyrecord')

        print("Connected to the database")

    def connect(self) -> None:
        """connect to the database
        and also create a session"""
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        Session = sessionmaker(bind=self._engine, expire_on_commit=False)
        session = scoped_session(Session)
        self._session = session

    @property
    def session(self):
        """establish a session"""
        return self._session
    
    def add_user(self, obj):
        """save user
        to db"""
        self.session.add(obj)
      
    def save(self):
        """save user
        to database"""
        self.session.commit()

    def find_user(self, obj, **kwargs):
        """find user based on keyworded
        args"""
        user = self._session.query(obj).filter_by(**kwargs).first()
        return user
    
    def update_user_info(self, obj, **kwargs):
        """update the user data
        in the database"""
        if not kwargs:
            raise ValueError('i am not kwargs')
        for k, v in kwargs.items():
            if hasattr(obj, k):
                setattr(obj, k, v)
        self.save()

    def delete(self, obj):
        """delete user
        from db"""
        self.session.delete(obj)