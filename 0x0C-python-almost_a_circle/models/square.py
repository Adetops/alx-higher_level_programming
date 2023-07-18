#!/usr/bin/python3
''' Module that defines a Square '''


from models.rectangle import Rectangle


class Square(Rectangle):
    ''' Implementing the Square class that inherits from Rectangle '''

    def __init__(self, size, x=0, y=0, id=None):
        ''' Initializing the Square and its properties
        Args:
            size (int): The size of the square
            x (int): the x coordinate of the square
            y (int): the y coordinate of the square
        '''

        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        ''' size (int): the square size '''

        return (self.width)

    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        if (value <= 0):
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        ''' String representation of Square class '''

        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}")

    def update(self, *args, **kwargs):
        ''' method that assigns an argument to each attribute
        Args:
            args (any): variable-length argument
            kwargs (any): assigns a key/value argument to attributes
        '''

        if len(args) > 0:
            vars = ['id', 'size', 'x', 'y']
            for idx, val in enumerate(args):
                setattr(self, vars[idx], val)
        elif len(kwargs) > 0:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        ''' dictionary representation of a Square '''

        return {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
