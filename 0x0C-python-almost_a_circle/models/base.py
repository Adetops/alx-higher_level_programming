#!/usr/bin/python3
''' Module that defines the base init for this project '''
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        ''' JSON string representation of list_dictionaries
        Args:
            list_dictionaries (list): list of dictionaries

        Return:
            The JSON string representation
        '''

        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' writes the JSON string representation of list_objs to a file '''

        filename = cls.__name__ + ".json"
        list_obj = []
        with open(filename, "w") as f:
            if list_objs is None:
                f.write('[]')
            if list_objs is not None:
                for i in range(len(list_objs)):
                    json_not = Base.to_json_string(list_objs[i])
                    list_obj.append(json_not)
            f.write(list_obj)
