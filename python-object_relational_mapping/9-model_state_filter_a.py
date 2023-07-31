#!/usr/bin/python3
"""
Lists all State objects that contain the letter "a" from the
    database hbtn_0e_6_usa.

Usage:
    python3 9-model_state_filter_a.py mysql_username mysql_password
        database_name

The script takes three command-line arguments:
    - mysql_username (str): The MySQL database username.
    - mysql_password (str): The MySQL database password.
    - database_name (str): The name of the MySQL database.

Make sure you have the required MySQL connector library installed for Python.

Example:
    python3 9-model_state_filter_a.py root root hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def filter_states_with_a(mysql_username, mysql_password, database_name):
    # Create an engine to connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(mysql_username, mysql_password,
                                   database_name),
                           pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects that contain the letter "a" and sort them
    #   by states.id
    states_with_a = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all()

    # Print the State objects in the desired format
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # Close the session
    session.close()


if __name__ == "__main__":
    # The script expects three command-line arguments: MySQL username,
    #   password, and database name
    mysql_username, mysql_password, database_name = sys.argv[1],\
        sys.argv[2], sys.argv[3]

    # Call the function with the provided arguments
    filter_states_with_a(mysql_username, mysql_password, database_name)
