#!/usr/bin/python3
""" Define a square:"""


class Square:
    """implementing the class square """

    def __init__(self, size=0, position=(0, 0)):
        """ Initializing the square now

        Args:
            size: the size of the square
            position: private instance attribute
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ position (tuple): position getter and setter """
        return self.__position

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or (len(value) != 2) or
                not all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ Public instance method """
        return self.__size ** 2

    def my_print(self):
        """ public instance that prints in standard output. """
        if (self.__size == 0):
            print()
            return

        [print() for i in range(0, self.__position[1])]

        for length in range(self.__size):
            for val in range(self.__position[0]):
                [print(" ", end="")]
            for breadth in range(self.__size):
                [print("#", end="")]
            print()
