#!/usr/bin/python3
""" Define a square: must use property."""


class Square:
    """implementing the class square """

    def __init__(self, size=0):
        """ Initializing the square now

        Args:
            size: the size of the square
        """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
