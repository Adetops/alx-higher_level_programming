#!/usr/bin/python3
''' Module that defines a class BaseGeometry'''


class BaseGeometry:
    ''' An class that has only one method '''

    def area(self):
        ''' Method that raises an exception '''

        raise Exception("area() is not implemented")
