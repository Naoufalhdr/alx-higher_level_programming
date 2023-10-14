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
        """
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Serialize a list of instances and save them as JSON data to a file.

        Args:
            cls: The class itself, used to determine the filename.
            list_objs (list): A list of instances to be serialized and saved.
        """
        if list_objs is None:
            list_objs = []

        file_name = f"{cls.__name__}.json"
        obj_dicts = [obj.to_dictionary() for obj in list_objs]

        with open(file_name, "w", encoding="utf-8") as file:
            file.write(Base.to_json_string(obj_dicts))

    @classmethod
    def load_from_file(cls):
        """
        Load a list of instances from a JSON file.

        Args:
            cls: The class itself.
        """
        file_name = f"{cls.__name__}.json"

        try:
            with open(file_name, "r", encoding="utf-8") as file:
                json_string = file.read()
                if json_string:
                    dict_list = Base.from_json_string(json_string)
                    instance_list = [cls.create(**item) for item in dict_list]
        except FileNotFoundError:
            return []

        return instance_list

    @classmethod
    def create(cls, **dictionary):
        """
        Create a new instance of the class with attributes set from a
        dictionary

        Args:
            cls: The class itself.
            **dictionary: A dictionary containing attribute values for the new
                          instance.

        Returns:
            A new instance of the class with attributes set according to the
            dictionary.
        """
        if dictionary:
            dummy = cls(1, 1) if cls.__name__ == "Rectangle" else cls(1)
            dummy.update(**dictionary)
            return dummy
