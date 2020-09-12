#!/usr/bin/env python

# imports
# from src.core.util import Crawler

# TODO write the below todo in multiline comment
# TODO ideally there should be a common parser class and then subclass for each language for now creating a common one and adding python parser in it

"""
This class contain parser methods for different languages
"""
class Parser():

    def getTODOPython(self,filename):
        """
        This function extract the to dos for a given file
        """
        # There are two ways todo can be in a file after # or inside """
        todoList = list()
        with open(filename) as f:
            lines = f.readlines()
            for line in lines():
                if line.strip()[0] == "#":
                    # TODO will modify the logic to adapt variants of todo
                    # using a temp varibale to make code more readable
                    lineLower = line.lower()
                    if "todo" in lineLower:
                        todoList.append(lineLower[lineLower.find("todo")+4:].strip())
        return todoList
