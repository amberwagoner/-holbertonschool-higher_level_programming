#!/usr/bin/python3
""" Defines an inhertied class function """


def inherits_from(obj, a_class):
    """ Returns True if the object is an instance of inherited class """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
