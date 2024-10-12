#!/usr/bin/python3
"""database class"""
from models import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

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
            'mysql+mysqldb://easyrecord:record \
            @localhost:5000/Easyrecord')

    def connect(self) -> None:
        """connect to the database
        and also create a session"""
        Base.metadata.create_all(self._engine)
       

    @property
    def session(self):
        """establish a session"""
        if self._session is None:
            Session = sessionmaker(bind=self._engine)
            self._session = Session()
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
        user = self._session.query(obj).filter_by(**kwargs)
        return user

    def delete(self, obj):
        """delete user
        from db"""
        self.session.delete(obj)