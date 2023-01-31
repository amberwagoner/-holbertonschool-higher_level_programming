#!/usr/bin/python3
""" Function that returns an object """
import json


def from_json_string(my_str):
    """ Returns an object respresented by JSON string """

    return json.loads(my_str)
