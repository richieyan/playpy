# coding: utf-8

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqldb://root@localhost:3306/blog?charset=utf8')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()




Base.metadata.create_all(engine)





