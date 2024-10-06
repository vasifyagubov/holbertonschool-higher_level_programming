#!/usr/bin/python3

"""writing to a file"""


def write_file(filename="", text=""):
    """Function"""
    with open(filename, 'w', encoding='utf-8') as file:
        return (file.write(text))
