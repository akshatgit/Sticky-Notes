#!/usr/bin/env python

# imports
from src.core.util.todo import Todo

# TODO write the below todo in multiline comment
# TODO ideally there should be a common parser class and then subclass for each language for now creating a common one and adding python parser in it

class Parser():

    def __init__(self, **kwargs):
        """
        Constructor of parser class
        """
        self.__code_files = kwargs.get("code_files")
        self.parsed_todo = {
            "Python" : list(),
            "HTML" : list()
        }
        self.supported_languages=["Python", "HTML"]
        self.todo_list = list()


    def get_todo_list(self):
        factory = parserFactory()
        for language in self.__code_files:
            parser = factory.get_parser(language)
            for filepath in self.__code_files[language]:
                todos_of_file = parser.parse(filepath) # TODO Optimize this line
                if todos_of_file is not None:
                    self.todo_list += todos_of_file
        return self.todo_list
    

class parserFactory:

    __instance = None
    
    @staticmethod
    def getInstance():
        # Static Access Method
        if parserFactory.__instance == None:
            parserFactory()

    def __init__(self):
        if parserFactory.__instance != None:
            raise Exception("Parser Factory is a singleton class")
        else:
            parserFactory.__instance = self 


    # This will return the appropriate parser
    def get_parser(self, language):
        if language == "Python":
            return pythonTodoParser()
        elif language == "HTML":
            return htmlTodoParser()
        else:
            raise ValueError(language)
            

class pythonTodoParser:

    def __init__(self):
        self.language = "Python"

    def parse(self, filename):
        todo_list = list()
        with open(filename) as f:
            lines = f.readlines()
            for i in range(0, len(lines)):
                if "#" in lines[i]: # since comment can be after the code as well
                    stripedLine = lines[i][lines[i].find("#"):].strip().lower()
                    if "todo" in stripedLine:
                        todo = Todo(todo_header=stripedLine[stripedLine.find("todo")+4:].strip(), todo_body=None, file_path=filename, line_no=i+1)
                        todo_list.append(todo)
        if len(todo_list) > 0:
            return todo_list
        else:
            return None


class htmlTodoParser:

    def __init__(self):
        self.language = "HTML"

    def parse(self, filename):
        todo_list = list()
        with open(filename) as f:
            lines = f.readlines()
            for i in range(0, len(lines)):
                if "#" in lines[i]: # since comment can be after the code as well
                    stripedLine = lines[i][lines[i].find("<!--"):].strip().lower()
                    if "todo" in stripedLine:
                        todo = Todo(todo_header=stripedLine[stripedLine.find("todo")+4:].strip().rstrip("-->"), todo_body=None, file_path=filename, line_no=i+1)
                        todo_list.append(todo)
        if len(todo_list) > 0:
            return todo_list
        else:
            return None


