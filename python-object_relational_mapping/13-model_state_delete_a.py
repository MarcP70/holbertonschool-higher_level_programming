#!/usr/bin/python3
"""
Deletes all State objects with a name containing the letter "a"
from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def delete_states_with_a(mysql_username, mysql_password, database_name):
    """
    Deletes all State objects with a name containing the letter "a"
    from the database.

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

    # Query and delete all State objects with a name containing the letter "a"
    states_with_a = session.query(State).filter(State.name.ilike('%a%')).all()
    for state in states_with_a:
        session.delete(state)
    session.commit()

    # Close the session
    session.close()


if __name__ == "__main__":
    # The script expects three command-line arguments: MySQL username,
    #   password, and database name
    mysql_username, mysql_password, database_name =\
        sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function with the provided arguments
    delete_states_with_a(mysql_username, mysql_password, database_name)
