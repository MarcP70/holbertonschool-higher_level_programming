#!/usr/bin/python3
"""
This script retrieves and prints all the states from the 'states' table
in a MySQL database with names starting with 'N'.
"""
import MySQLdb
import sys


def get_all_states(mysql_username, mysql_password, database_name):
    """
    Lists all states with names starting with 'N' from the given
        MySQL database.

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

    # Execute the SQL query to retrieve all rows from the 'states' table
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

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
    mysql_username, mysql_password, database_name = sys.argv[1],\
        sys.argv[2], sys.argv[3]

    # Call the get_all_states function with the provided arguments
    get_all_states(mysql_username, mysql_password, database_name)
