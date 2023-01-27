#!/usr/bin/python3
"""Defines function that checks class"""


def is_same_class(obj, a_class):
    """Returns true if obj is an instance of speciifed class"""
    return type(obj) is a_class
