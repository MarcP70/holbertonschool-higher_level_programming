#!/usr/bin/python3
def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: An object to inspect.

    Returns:
        A list of strings representing the attributes and methods
            of the object.
    """
    attributes = []
    methods = []

    for attr_name in dir(obj):
        attr = getattr(obj, attr_name)
        if callable(attr):
            methods.append(attr_name)
        else:
            attributes.append(attr_name)

    return attributes + methods
