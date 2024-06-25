#!/usr/bin/python3
"""This module is for task 8"""
import sys
from mysqlalchemy.orm import sessionmaker
from mysqlalchemy import (create_engine)
from model_state import Base, State


if __name__ == "__main__":
    engine = ceate_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                          .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    state_table = session.query(State).first()
    if state_data is None:
        print("Nothing")
    else:
        print(state_data.id, state_data.name, sep": ")
