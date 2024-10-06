#!usr/bin/python3

"""Creatinng new filwe"""

def read_file(filename=""):
    """Function"""
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end="")
