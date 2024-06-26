#!/usr/bin/python3
""" Lists all City objects and corresponding State objects contained in
the database hbtn_0e_100_usa """

import sys
from relationship_state import State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).all()
    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")

    session.close()
