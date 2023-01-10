#!/usr/bin/python3
""" defining funtion"""
import json


def to_json_string(my_obj):
     """Return the JSON representation of a string object."""
     return json.dump(my_obj)
