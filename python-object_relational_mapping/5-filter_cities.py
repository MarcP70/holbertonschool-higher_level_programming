#!/usr/bin/python3

"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
"""
import MySQLdb
import sys


def filter_cities_by_state(mysql_username, mysql_password,
                           database_name, state_name):
    """
    Lists all cities of a given state from the database hbtn_0e_4_usa.

    Parameters:
        mysql_username (str): The MySQL database username.
        mysql_password (str): The MySQL database password.
        database_name (str): The name of the MySQL database.
        state_name (str): The name of the state to filter cities.

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

    # Prepare the SQL query with user input using a placeholder (%s)
    query = (
        "SELECT GROUP_CONCAT(cities.name SEPARATOR ', ') "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC"
    )
    cursor.execute(query, (state_name,))

    # Fetch the single value returned by the query
    result = cursor.fetchone()[0]

    # Print the result (cities) for the given state
    if result is not None:
        print(result)
    else:
        print()

    # Close the cursor and the database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # The script expects four command-line arguments: MySQL username,
    # password, database name, and state name
    mysql_username, mysql_password, database_name, state_name = (
        sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    )

    # Call the filter_cities_by_state function with the provided arguments
    filter_cities_by_state(mysql_username, mysql_password,
                           database_name, state_name)
