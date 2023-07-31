#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa.
"""

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def fetch_cities_by_state(mysql_username, mysql_password, database_name):
    """
    Fetches and prints all City objects from the database hbtn_0e_14_usa.

    Parameters:
        mysql_username (str): The MySQL database username.
        mysql_password (str): The MySQL database password.
        database_name (str): The name of the MySQL database.

    Returns:
        None
    """

    # Create an engine to connect to the MySQL database
    engine = create_engine(f'mysql+mysqldb://{mysql_username}:{mysql_password}\
                           @localhost/{database_name}', pool_pre_ping=True)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all City objects and their corresponding state names,
    #   sorted by city id
    cities = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id).all()

    # Print the results in the specified format
    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    # Close the session
    session.close()


if __name__ == "__main__":
    # The script expects three command-line arguments: MySQL username,
    #   password, and database name
    mysql_username, mysql_password, database_name =\
        sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function with the provided arguments
    fetch_cities_by_state(mysql_username, mysql_password, database_name)
