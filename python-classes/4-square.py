#!/usr/bin/python3
"""
This module contains a class Square that defines a square by its size.
"""


class Square:
    """Represents a square with a private size attribute."""

    def __init__(self, size=0):
        """
        Initialize the square with a given size.
        Type must be int and value must be >= 0.
        """
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.
        Raises TypeError if value is not an integer.
        Raises ValueError if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with # characters."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
