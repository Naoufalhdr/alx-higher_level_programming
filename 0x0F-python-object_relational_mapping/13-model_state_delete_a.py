#!/usr/bin/python3
""" Delete all the State object with a name containing the letter 'a'
from the database """

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    state_to_delete = session.query(State).filter(State.name.like('%a%')).all()
    for row in state_to_delete:
        session.delete(row)
    session.commit()
    session.close()
