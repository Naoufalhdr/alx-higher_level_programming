#!/usr/bin/python3
"""Defines an empty class BaseGeometry"""


class BaseGeometry:
    """A base class for geometry-related classes."""

    def area(self):
        """
        Raises an Exception indicating that the area() method is not
        implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the input value

        Args:
            name (str): The name of the value being validated.
            value: The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
