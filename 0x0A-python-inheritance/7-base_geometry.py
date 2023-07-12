#!/usr/bin/python3
''' Module that defines a class BaseGeometry'''


class BaseGeometry:
    ''' An class that defines geometry functions

    Methods:
        area(self): raises an exception
        integer_validator(self, name, value): validates a value
    '''

    def area(self):
        ''' Method that raises an exception '''

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        ''' Method that validates a value
        Args:
            name (str): a string name
            value (int): an integer value
        '''

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if (value <= 0):
            raise ValueError("{} must be greater than 0".format(name))
