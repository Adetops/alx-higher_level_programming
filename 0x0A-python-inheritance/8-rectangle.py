#!/usr/bin/python3
''' Modules that defines the class Rectangle '''


BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    '''A class that inherits from BaseGeometry'''

    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__heigth = height
