#!/usr/bin/python3
"""
Prints the State object with the name passed as an argument from the
    database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_state_id(mysql_username, mysql_password, database_name, state_name):
    """
    Prints the State object's ID with the given state_name.

    Parameters:
        mysql_username (str): The MySQL database username.
        mysql_password (str): The MySQL database password.
        database_name (str): The name of the MySQL database.
        state_name (str): The state name to search in the states table.

    Returns:
        None
    """

    # Create an engine to connect to the MySQL database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(mysql_username, mysql_password,
                                   database_name),
                           pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query the State object with the given state_name
    state = session.query(State).filter(State.name == state_name).first()

    # Check if the state exists
    if state is None:
        print("Not found")
    else:
        # Print the state's ID
        print(state.id)

    # Close the session
    session.close()


if __name__ == "__main__":
    # The script expects four command-line arguments: MySQL username,
    #   password, database name, and state name to search
    mysql_username, mysql_password, database_name, state_name_to_search =\
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Call the function with the provided arguments
    get_state_id(mysql_username, mysql_password,
                 database_name, state_name_to_search)
