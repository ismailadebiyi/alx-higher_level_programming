#!/usr/bin/python3
""" view all city in a state """

from model_state import Base, State
from model_city import City
from sys import argv, exit
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    if len(argv) != 4:
        print("Usage: ./14.py <username> <password> <database>")
        exit(1)

    try:
        engine = create_engine('mysql://{}:{}@localhost:3306/{}'
                               .format(argv[1], argv[2], argv[3]))
    except Exception as err:
        print(err)
        exit(1)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State.name, City.id, City.name)
                          .filter(State.id == City.state_id)
    for instance in query:
        print(instance[0] + ": (" + str(instance[1]) + ") " + instance[2])
