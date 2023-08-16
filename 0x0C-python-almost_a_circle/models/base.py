#!/usr/bin/python3
''' Module that defines the base init for this project '''
import json
import os


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

        if list_dictionaries is None or bool(list_dictionaries) is False:
            return "[]"
        else:
            New = json.dumps(list_dictionaries)
            return (New)

    @classmethod
    def save_to_file(cls, list_objs):
        ''' writes the JSON string representation of list_objs to a file '''

        file = "{}.json".format(cls.__name__)
        obj_list = []
        with open(file, "w") as file_obj:
            if list_objs is None:
                JStr = Base.to_json_string(obj_list)
            else:
                for i in range(len(list_objs)):
                    obj_list.append(list_objs[i].to_dictionary())
                    JStr = Base.to_json_string(obj_list)
            file_obj.write(JStr)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of JSON string representation"""

        if json_string is None or bool(json_string) is False:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""

        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Returns a list of intances"""

        file = "{}.json".format(cls.__name__)
        instances = []
        if os.path.isfile(file):
            with open(file, "r", encoding="UTF-8") as file_obj:
                for dictionary in cls.from_json_string(file_obj.read()):
                    instances.append(cls.create(**dictionary))
        return instances

@classmethod
def save_to_file_csv(cls, list_objs):
    filename = cls.__name__ + '.csv'
    obj_list = []
    if list_objs is not None:
        for objs in list_objs:
            dic = objs.to_dictionary()
            obj_list.append(dic)
    rectangle_header = ['id', 'width', 'height', 'x', 'y']
    square_header = ['id', 'size', 'x', 'y']
    with open(filename, "w") as csvfile:
        if list_objs is None:
            Cobj = []
        else:
            if cls.__name__ == 'Rectangle':
                head = csv.writeheader(rect)
            for i in range(len(list_objs)):
                obj_list.append(list_objs[i].to_dictionary())
                JStr = Base.to_json_string(obj_list)
            file_obj.write(JStr)
@classmethod
def load_from_file_csv(cls):