#!/usr/bin/python3
"""Defines a Square class with a private size attribute."""


class Square:
    """Represents a square."""

    def __init__(self, size):
        """Initialize a Square with a given size.

        Args:
            size: The size of the square (no validation yet).
        """
        self.__size = size
