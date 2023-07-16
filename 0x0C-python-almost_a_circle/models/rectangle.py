#!/usr/bin/python3
''' Module that defines a rectangle '''


from models.base import Base

class Rectangle(Base):
    ''' Implementing the Rectangle class that inherits from Base '''

    def __init__(self, width, height, x=0, y=0, id=None):
        ''' Initializing the Rectangle and its properties
        Args:
            width (int): The width of the rectangle
            height (int): The height of the rectangle
            x (int): the position of the rectangle on the latitude
            y (int): the position of the rectangle on the longitude
        '''

        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        ''' width (int): the rectangle width '''
        return (self.__width)

    @width.setter
    def width(self):
        self.__width = self.__width

    @property
    def height(self):
        ''' height (int): the rectangle height '''
        return (self.__height)

    @height.setter
    def height(self):
        self.__height = self.__height

    @property
    def x(self):
        ''' x (int): horizontal axis '''
        return (self.__x)

    @x.setter
    def x(self):
        self.__x = self.__x

    @property
    def y(self):
        ''' y (int): vertical axis '''
        return (self.__y)

    @y.setter
    def y(self):
        self.__y = self.__y
