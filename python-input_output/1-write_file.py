#!/usr/bin/python3

"""Appending to a file"""


def append_write(filename="", text=""):
    """Function"""
    with open(filename, 'w', encoding='utf-8') as file:
        return (file.write(text))
