#!/usr/bin/python3
"""
This module includes a class MyList that inherits from list.
"""


class MyList(list):
    """
    This class that inherits from list and provides additional functionality.
    Parameters:
        - list: The list class.
    """

    def __init__(self):
        """
        This methode initializes a new instance of the MyList class.
        Parameters:
        - self: The list instance being initialized.
        """

        super().__init__()
        pass

    def print_sorted(self):
        """
        Prints the list in ascending order.
        """

        print(sorted(self))
