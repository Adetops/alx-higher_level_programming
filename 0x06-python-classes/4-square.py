#!/usr/bin/python3
""" Define a square:"""


class Square:
    """implementing the class square """

    def __init__(self, size=0):
        """ Initializing the square now

        Args:
            size: the size of the square
        """
        self.__size = size

    @property
    def size(self):
        """ size (int): just to get the size """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ Public instance method """
        return self.__size ** 2
