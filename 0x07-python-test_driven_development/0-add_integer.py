#!/usr/bin/python3
"""This module defines a function add_integer()"""

def add_integer(a, b=98):
	""" A function that returns the sum of its arguments

	Args:
		a (int): can either be an int or float, if it's a float, it is converted to int
		b (int, optional): same as first arg. Defaults to 98.

	Returns:
		(int): the sum of a and b
	"""
    return a+b
