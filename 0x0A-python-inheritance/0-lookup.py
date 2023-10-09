#!/usr/bin/python3


def lookup(obj):
    """
    Return a list of attributes and methods associated with the given object.

    Parameters:
    obj (object): The Python object whose attributes and methods are to be
                  listed.

    Returns:
    list: A list containing the names of attributes and methods associated
          with the object.
    """
    return dir(obj)
