#!/usr/bin/python3
"""Module containing print_sorted func"""

class Mylist(list):

    """Class inherited from list class"""

    def print_sorted(self):
        """Method to print sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
