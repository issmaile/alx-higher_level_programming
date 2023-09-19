#!/usr/bin/python3

"""Defines a base model class"""
import json
import csv
import turtle


class Base:
    """
    This represents the base for all other classes in this project

    Private Class Attributes:
        __nb_objects (int): Num of instantiated base
    """

    __np_objects = 0

    def __init__(self, id=None):
        """Inits a new Base

        Args:
        id (int): The identity of the new Base
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return the JSON serialization of a list of dictions.

        Args:
            list_dictionaries (list): A list of dicts.
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the Json serialization of a lisat of obs to a file

        Args:
            list_objs (list): A list of inherited Base instancves.
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jf:
            if list_objs is None:
                jf.write("[]")
            else
            list_dicts = [o.to_dictionary() for o in list_objs]
            jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a Json str

        Args:
            json_string (str): A Json str representation of alist of dics
        Returns:
            If json_string is None or empty: an empty list
            Else - the Python list rpepresented by json_string
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Return a class instanstaied from a dict of attrs

        Aregs:
            **dictionary (dict): Key/value paris of attrs to init.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of classes instanced from a file of JSOn strs.

        Reads from `<cls.__name__>.json`

        Returns:
            If the file does not exist: empty klist
            ELse: a list of instantiaed classes
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jf:
                list_dicts = Base.from_json_string(jf.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Write the CSV serializationa se of a list of objects to a lfile

        Args:
            list_Objs (list): A list of inherited Base instances
        """
        filename = cls.__name__ + ".json"
        with open(filename, "w", newline="") as cf:
            if list_objs is None or list_objs == []:
                cf.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(cf, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """
        Return  a list of classes instaced from a CSV file

        Reads from `<cls.__name__>.csv`

        Returns:
            if the file doesnt exeist: an empty list
            else: a list of instantiaed classes
        """
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, "r", newline="") as cf:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(cf, fieldnames=fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in dic.items())
                        for dic in list_dicts]
                return [cls.create(**d) for dic in list_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """
        Drwa a Rectangle and Squares using the turtle module

        Args:
            list_rectangles (list): A list of Rectangle s to draw.
            list_squares (list): A list of Square s to draw
        """
        trt = turtle.Turtle()
        trt.screen.bgcolor("#222423")
        trt.pensize(3)
        trt.shape("turtle")

        trt.color("#f0fff7")
        for rect in list_rectangles:
            trt.showturtle()
            trt.up()
            trt.goto(rect.x, rect.y)
            trt.down()
            for i in range(2):
                trt.forward(rect.width)
                trt.left(90)
                trt.forward(rect.height)
                trt.left(90)
            trt.hideturtle()

        trt.color("#82aaff")
        for sqr in list_squares:
            trt.showturtle()
            trt.up()
            trt.goto(sqr.x, sqr.y)
            trt.down()
            for i in range(2):
                trt.forward(sqr.width)
                trt.left(90)
                trt.forward(sqr.height)
                trt.left(90)
            trt.hideturtle()

        turtle.exitonclick()
