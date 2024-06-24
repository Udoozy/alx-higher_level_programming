#!/usr/bin/python3
"""This Define a Base AND Base Class"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, create_engine

Base = declarative_base()


class State(Base):
    """State class"""
    __tablename__ = 'states'
    id = Column(
            Integer,
            primary_key=True,
            autoincrement=True,
            nullable=False
            )
    name = Column(String(128), nullable=False)
