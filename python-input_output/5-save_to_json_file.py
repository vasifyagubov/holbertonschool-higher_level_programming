#!/usr/bin/python3

"""Save objects to a file"""
import json


def save_to_json_file(my_obj, filename):
    """Function"""
    with open(filename, encoding='utf8') as file:
        a=json.dumps(my_obj)
        return (file.write(a))
