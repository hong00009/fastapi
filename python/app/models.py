# coding: utf-8
from sqlalchemy import (Column, String, text, CHAR, DateTime)
from sqlalchemy.dialects.mysql import INTEGER, TINYINT
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = "user"

    id = Column(INTEGER, primary_key=True)
    user_id = Column(String(255))
    name = Column(String(255))
    password = Column(String(255))
    type = Column(CHAR(1))
    createdAt = Column(DateTime)
    location = Column(String(255))