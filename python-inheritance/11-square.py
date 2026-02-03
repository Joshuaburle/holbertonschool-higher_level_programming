#!/usr/bin/python3
"""Module that defines a Square class with custom string representation."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class inheriting from Rectangle."""

    def __init__(self, size):
        """Initializes a Square with validated private size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Returns the area of the Square."""
        return self.__size * self.__size

    def __str__(self):
        """Returns the string representation of the Square."""
        return "[Square] {}/{}".format(self._Rectangle__width,
                                        self._Rectangle__height)
