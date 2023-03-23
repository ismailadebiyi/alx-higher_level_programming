#!/usr/bin/python3
""" Lists all states from a database """

if __name__ == "__main__":
    import sqlalchemy
    from model_state import Base, State
    from sys import argv, exit

    if len(argv) != 4:
        print("Usage: ./7.py <username> <password> <database>")
        exit(1)

    usr, pwd, dbe = argv[1], argv[2], argv[3]

    eng = "mysql://" + usr + ":" + pwd + "@localhost:3306/" + dbe
    try:
        engine = sqlalchemy.create_engine(eng)
    except Exception as err:
        print(err)
        exit(1)

    Base.metadata.create_all(engine)
    Session = sqlalchemy.orm.sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        if states is None:
            print("None")
        else:
            print(instance.id, instance.name, sep=": ")
