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
    def width(self, value):
        if (type(value) != int):
            raise TypeError("width must be an integer")
        elif (value <= 0):
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        ''' height (int): the rectangle height '''

        return (self.__height)

    @height.setter
    def height(self, value):
        if (type(value) != int):
            raise TypeError("height must be an integer")
        elif (value <= 0):
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        ''' x (int): horizontal axis '''

        return (self.__x)

    @x.setter
    def x(self, value):
        if (type(value) != int):
            raise TypeError("x must be an integer")
        elif (value < 0):
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        ''' y (int): vertical axis '''

        return (self.__y)

    @y.setter
    def y(self, val):
        if (type(val) != int):
            raise TypeError("y must be an integer")
        elif (val < 0):
            raise ValueError("y must be >= 0")
        self.__y = val

    def area(self):
        ''' method returns the area of rectangle '''

        return (self.__height * self.__width)

    def display(self):
        ''' prints in stdout the Rectangle instance with the character # '''

        for r in range(self.__y):
            print()
        for i in range(self.__height):
            print((' ' * self.x) + ('#' * self.width))

    def __str__(self):
        ''' String representation of Rectangle class '''

        return (f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - \
{self.__width}/{self.__height}")

    def update(self, *args, **kwargs):
        ''' method that assigns an argument to each attribute
        Args:
            args (any): variable-length argument
            kwargs (any): assigns a key/value argument to attributes
        '''

        if len(args) > 0:
            vars = ['id', 'width', 'height', 'x', 'y']
            for idx, val in enumerate(args):
                setattr(self, vars[idx], val)
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)
