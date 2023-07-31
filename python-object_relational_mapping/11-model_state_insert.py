#!/usr/bin/python3
"""
Adds the State object "Louisiana" to the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def add_state(mysql_username, mysql_password, database_name):
    """
    Adds the State object "Louisiana" to the database.

    Parameters:
        mysql_username (str): The MySQL database username.
        mysql_password (str): The MySQL database password.
        database_name (str): The name of the MySQL database.

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

    # Create the State object with the name "Louisiana"
    new_state = State(name="Louisiana")

    # Add the new State object to the session and commit the changes
    #   to the database
    session.add(new_state)
    session.commit()

    # Print the new state's ID after creation
    print(new_state.id)

    # Close the session
    session.close()


if __name__ == "__main__":
    # The script expects three command-line arguments: MySQL username,
    #   password, and database name
    mysql_username, mysql_password, database_name =\
        sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function with the provided arguments
    add_state(mysql_username, mysql_password, database_name)
