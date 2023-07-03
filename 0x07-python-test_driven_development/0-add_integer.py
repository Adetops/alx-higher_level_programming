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
    if ((not isinstance(a, int)) and (not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int)) and (not isinstance(b, float))):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
