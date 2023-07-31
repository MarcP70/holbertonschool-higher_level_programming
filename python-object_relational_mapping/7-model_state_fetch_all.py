#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # The script expects three command-line arguments:
    #   MySQL username, password, and database name
    mysql_username, mysql_password, database_name =\
        sys.argv[1], sys.argv[2], sys.argv[3]

    # Create an engine to connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(mysql_username, mysql_password,
                                   database_name),
                           pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects from the database and sort by states.id
    states = session.query(State).order_by(State.id).all()

    # Print the State objects in the desired format
    for state in states:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()
