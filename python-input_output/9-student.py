#!/usr/bin/python3

"""Student to JSON"""



class Student:
    """Student"""
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last__name
        self.age = age

        def to_json(self):
            """To JSON"""
            return self.__dict__
