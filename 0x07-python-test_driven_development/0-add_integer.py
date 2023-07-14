#!/usr/bin/python3

"""This module defines a function add_integer()"""


def add_integer(a, b=98):
    """ This function adds two integers together
    Args:
        a (int): the first argument
        b (int, optional): the second argument. Default is 98
    Returns:
        (int): the result of a + b
    """
    if ((type(a) != int) and (type(a) != float)):
        raise TypeError("a must be an integer")
    if ((type(b) != int) and (type(b) != float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
