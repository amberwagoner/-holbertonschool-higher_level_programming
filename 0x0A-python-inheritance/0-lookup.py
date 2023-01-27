#!/usr/bin/python3
""" Defines lookup prototype """


def lookup(obj):
    """ Returns list of object's available attributes and methods """
    return (dir(obj))
