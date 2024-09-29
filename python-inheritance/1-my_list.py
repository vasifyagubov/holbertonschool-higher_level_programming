#!/usr/bin/python3
"""Module containing print_sorted func"""

class Mylist(list):
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
