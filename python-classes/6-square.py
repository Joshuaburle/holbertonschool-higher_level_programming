#!/usr/bin/python3
"""Defines a Square class with size and position."""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a Square with a given size and position.

        Args:
            size (int): The size of the square.
            position (tuple): The position offset (x, y).
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation."""
        if (
            not isinstance(value, tuple)
            or len(value) != 2
            or not isinstance(value[0], int)
            or not isinstance(value[1], int)
            or value[0] < 0
            or value[1] < 0
        ):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """Print the square using #, offset by position."""
        if self.__size == 0:
            print()
            return

        # vertical offset: print empty lines, NOT spaces
        for _ in range(self.__position[1]):
            print()

        # horizontal offset: print leading spaces on each square line
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
