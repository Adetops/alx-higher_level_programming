#!/usr/bin/python3
''' Module that defines the base init for this project '''


class Base:
    ''' Implementing the Base class '''

    __nb_objects = 0

    def __init__(self, id=None):
        ''' The Base class instatiation '''

        if (id is not None):
            self.id = id
        if (id is None):
            type(self).__nb_objects += 1
            self.id = type(self).__nb_objects
