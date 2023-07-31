#!/usr/bin/python3
"""
Changes the name of a State object from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def update_state(mysql_username, mysql_password, database_name):
    """
    Changes the name of the State object with id=2 to "New Mexico"
        in the database.

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

    # Query the State object with id=2
    state = session.query(State).filter(State.id == 2).first()

    # Update the name of the State object to "New Mexico"
    if state is not None:
        state.name = "New Mexico"
        session.commit()

    # Close the session
    session.close()


if __name__ == "__main__":
    # The script expects three command-line arguments: MySQL username,
    #   password, and database name
    mysql_username, mysql_password, database_name =\
        sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function with the provided arguments
    update_state(mysql_username, mysql_password, database_name)
