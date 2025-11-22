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
    def size(self):
        """ Return the size"""
        return self.__size
    def size(self, value):
        if not isinstance(value,  int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
                                                                                                                                                                                                                                            

