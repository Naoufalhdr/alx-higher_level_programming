#!/usr/bin/python3
"""This module define a square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialize a Square instance.

        Args:
            size (int): Size of the square.
            x (int): X-coordinate of the square's position (default 0).
            y (int): Y-coordinate of the square's position (default 0).
            id (int): Unique identifier for the square (default None).
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string representation of the square"""
        return (
                f"[{self.__class__.__name__}] ({self.id}) {self.x}/{self.y} - "
                f"{self.width}"
                )
