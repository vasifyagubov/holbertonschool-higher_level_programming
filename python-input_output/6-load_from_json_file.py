#!/usr/bin/python3
"""Python"""
import json


def load_from_json_file(filename):
    """function of getting json file string to object"""
    with open(filename, 'r', encoding='utf-8') as f:
        a = json.loads(my_obj)
        return f.read(a)
