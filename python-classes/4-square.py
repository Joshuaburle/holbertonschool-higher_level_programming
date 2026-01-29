#!/usr/bin/python3
"""Defines a Square class with controlled access to size."""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initialize a Square with a given size.

        Args:
            size (int): The size of the square.
        """
        self.size = size  # triggers the setter

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): New size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size
