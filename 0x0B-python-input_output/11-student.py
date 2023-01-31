#!/usr/bin/python3
""" Defines a class Student """


class Student:
    """ Represents a student """

    def __init__(self, first_name, last_name, age):
        """ Initializes a new student """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Return dictionary representation of a Student
        If attrs is a list of strings, represent only those attributes
        """
        if type(attrs) == list:
            if all(type(attr) == str for attr in attrs):
                return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """ Replaces all attributes of Student """
        for key, value in json.items():
            setattr(self, key, value)
