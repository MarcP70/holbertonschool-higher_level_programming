#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.

Usage:
    python3 8-model_state_fetch_first.py mysql_username mysql_password
        database_name

The script takes three command-line arguments:
    - mysql_username (str): The MySQL database username.
    - mysql_password (str): The MySQL database password.
    - database_name (str): The name of the MySQL database.

Make sure you have the required MySQL connector library installed for Python.

Example:
    python3 8-model_state_fetch_first.py root root hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def print_first_state(mysql_username, mysql_password, database_name):
    # Create an engine to connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(mysql_username, mysql_password,
                                   database_name),
                           pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the first State object from the database based on states.id
    first_state = session.query(State).order_by(State.id).first()

    # Check if any state exists
    if first_state is None:
        print("Nothing")
    else:
        # Print the first State object in the desired format
        print("{}: {}".format(first_state.id, first_state.name))

    # Close the session
    session.close()


if __name__ == "__main__":
    # The script expects three command-line arguments: MySQL username,
    #   password, and database name
    mysql_username, mysql_password, database_name = sys.argv[1],\
        sys.argv[2], sys.argv[3]

    # Call the function with the provided arguments
    print_first_state(mysql_username, mysql_password, database_name)
