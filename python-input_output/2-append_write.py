#!/usr/bin/python3

"""Appending to a file"""


def append_write(filename="", text=""):
    """Function"""
    with open(filename, 'a', encoding='utf8') as file:
        return (file.append(), end="")
