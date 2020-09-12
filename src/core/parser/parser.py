#!/usr/bin/env python

# imports
# from src.core.util import Crawler

# TODO write the below todo in multiline comment
# TODO ideally there should be a common parser class and then subclass for each language for now creating a common one and adding python parser in it

"""
This class contain parser methods for different languages.
TODO convert the class to parserFactoy 
"""
class Parser():

    def getTODOPython(self,filename):
        """
        This function extract the to dos for a given file
        This will return the todo in this format 
        {"filepath":"path/to/file.py","todo":[(lineno,message)]}
        """
        # There are two ways todo can be in a file after # or inside """
        # Above line will also be returned by parser #logic :P 
        todoList = list()
        todoDict = dict()
        with open(filename) as f:
            lines = f.readlines()
            for i in range(0,len(lines)):
                if "#" in lines[i]: # since comment can be after the code as well
                    stripedLine = lines[i][lines[i].find("#"):].strip().lower()
                    # TODO will modify the logic to adapt variants of todo
                    if "todo" in stripedLine:
                        todoList.append( (i+1,stripedLine[stripedLine.find("todo")+4:].strip()) )
        if len(todoList) > 0:
            todoDict["filepath"] = filename
            todoDict["todo"] = todoList
            return todoList
        else:
            return None

# Stub Code to test parser
def parser_test():
    filename = "./parser.py"
    parser_obj = Parser()
    print(parser_obj.getTODOPython(filename))

parser_test()

