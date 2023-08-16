#!/usr/bin/python3
'''defines a and is also module Base class.'''
from json import dumps, loads
import csv


class Base:
    '''A representation of the base of our OOP hierarchy in the project.'''

    __nb_objects = 0

    def __init__(self, id=None):
        '''Constructor.'''
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        '''Jsonifies a dictionary so it's quite rightly and longer.'''
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
<<<<<<< HEAD
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
=======
            return dumps(list_dictionaries)
>>>>>>> 7716dd44864ad13b0c2b373010f0f7684f4a3b07

    @staticmethod
    def from_json_string(json_string):
        '''Unjsonifies a dictionary.'''
        if json_string is None or not json_string:
            return []
        return loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        '''Saves jsonified object to file.'''
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @classmethod
    def load_from_file(cls):
        '''Loads string from file and unjsonifies.'''
        from os import path
        file = "{}.json".format(cls.__name__)
<<<<<<< HEAD
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
=======
        if not path.isfile(file):
            return []
        with open(file, "r", encoding="utf-8") as f:
            return [cls.create(**d) for d in cls.from_json_string(f.read())]

    @classmethod
    def create(cls, **dictionary):
        '''Loads instance from dictionary.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if cls is Rectangle:
            new = Rectangle(1, 1)
        elif cls is Square:
            new = Square(1)
        else:
            new = None
        new.update(**dictionary)
        return new

    @classmethod
    def save_to_file_csv(cls, list_objs):
        '''Saves object to csv file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
        with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)

    @classmethod
    def load_from_file_csv(cls):
        '''Loads object to csv file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        ret = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                ret.append(cls.create(**d))
        return ret

    @staticmethod
    def draw(list_rectangles, list_squares):
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for i in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensize(1)
            t.penup()
            t.pendown()
            t.setpos((i.x + t.pos()[0], i.y - t.pos()[1]))
            t.pensize(10)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.end_fill()

        time.sleep(5)
>>>>>>> 7716dd44864ad13b0c2b373010f0f7684f4a3b07
