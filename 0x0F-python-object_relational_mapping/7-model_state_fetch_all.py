#!/usr/bin/python3
"""Module for task 7"""

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy.ext.declarative import declarative_base
    from model_state import Base, State
    import sys

    args = sys.argv
    if len(args) < 4:
        exit(1)
    str_con = 'mysql-mysqldb://{}:{}@localhost:3306/{}'
    engine = create_engine(str_con.format(args[1], args[2], args[3]))
    Make_sess = sessionmaker(bind=engine)

    Base.metadata.create_all(engine)
    session = Make_sess()

    result = session.query(State).order_by(State.id).all()
    for state in result:
        print("{}: {}".format(state.id, state.name))
    session.close()
