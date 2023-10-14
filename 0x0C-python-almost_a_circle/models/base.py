#!/usr/bin/python3
"""This module defines the Base class."""
import json


class Base:
    """The Base class manages unique IDs for instances of derived classes."""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a Base instance with a unique ID or a provided 'id'."""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Deserialize a JSON string to a list of dictionaries.

        Args:
            json_string (str): A JSON string.

        Returns:
            list: A list of dictionaries.
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        """
        if list_objs is None:
            list_objs = []

        file_name = f"{cls.__name__}.json"
        obj_dicts = [obj.to_dictionary() for obj in list_objs]

        with open(file_name, "w", encoding="utf-8") as file:
            file.write(Base.to_json_string(obj_dicts))
