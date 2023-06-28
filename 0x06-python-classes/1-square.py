#!/usr/bin/python3
"""Definine a square with instance attribute size."""


class Square:
    def __init__(self, size):
        """ The __init__ method takes only one arg.

        Args:
            size (no type/value verification): Size of the square.
        """

        self.__size = size
