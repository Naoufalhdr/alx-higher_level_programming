#!/usr/bin/python3
"""
This module defines the Base class.
The Base class manages unique IDs for instances of derived classes.
"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance with a unique ID or a provided 'id'."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
