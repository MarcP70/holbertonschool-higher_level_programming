#!/usr/bin/python3

"""
Lists all cities from the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys


def list_cities_by_state(mysql_username, mysql_password, database_name):
    """
    Lists all cities from the database hbtn_0e_4_usa.

    Parameters:
        mysql_username (str): The MySQL database username.
        mysql_password (str): The MySQL database password.
        database_name (str): The name of the MySQL database.

    Returns:
        None
    """

    # Connect to the MySQL database
    db = MySQLdb.connect(
        host="localhost", port=3306,
        user=mysql_username, passwd=mysql_password, db=database_name
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to retrieve all cities with their
    # corresponding state names
    query = (
        "SELECT cities.id, cities.name, states.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC"
    )
    cursor.execute(query)

    # Fetch all the rows returned by the query
    results = cursor.fetchall()

    # Print each row
    for row in results:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # The script expects three command-line arguments: MySQL username,
    # password, and database name
    mysql_username, mysql_password, database_name =\
          sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the list_cities_by_state function with the provided arguments
    list_cities_by_state(mysql_username, mysql_password, database_name)
