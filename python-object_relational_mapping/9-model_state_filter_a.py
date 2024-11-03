#!/usr/bin/python3
"""
Module
"""
from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(argv[1], argv[2], argv[3]))

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.contains('a'))\
        .order_by(State.id)

    if states is None:
        print("Nothing")
    else:
        for state in states:
            print("{}: {}".format(state.id, state.name))

    if session:
        session.close()
