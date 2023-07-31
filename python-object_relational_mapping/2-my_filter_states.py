#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa where name matches
the argument.
"""
import MySQLdb
import sys


def filter_states_by_name(mysql_username, mysql_password, database_name,
                          state_name_searched):
    """
    Displays all values in the states table of hbtn_0e_0_usa where name
    matches the given state_name_searched.

    Parameters:
        mysql_username (str): The MySQL database username.
        mysql_password (str): The MySQL database password.
        database_name (str): The name of the MySQL database.
        state_name_searched (str): The state name to search in
            the states table.

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

    # Prepare the SQL query with user input using the format method
    # to prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id"
    cursor.execute(query, (state_name_searched,))

    # Fetch all the rows returned by the query
    results = cursor.fetchall()

    # Print each row
    for row in results:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # The script expects four command-line arguments: MySQL username,
    # password, database name, and state name to search
    mysql_username, mysql_password, database_name, state_name_searched =\
          sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

    # Call the filter_states_by_name function with the provided arguments
    filter_states_by_name(mysql_username, mysql_password,
                          database_name, state_name_searched)
