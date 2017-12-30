# coding: utf-8
from sqlalchemy import Column, String, Integer

class User(Base):

    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(64), nullable=False, index=True)
    password = Column(String(64), nullable=False)
    email = Column(String(64), nullable=False, index=True)


    def __repr__(self):
        return '%s(%r)' % (self.__class__.__name__, self.username)