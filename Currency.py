import os, csv  # import os and csv modules for csv reader

class Currency:
    """Currency class to hold information about a currency code"""
    def __init__(self, country, name, code):
        self.country = country
        self.name = name
        self.code = code

    def __str__(self):
        return "{}: {}".format(self.code, self.name)
