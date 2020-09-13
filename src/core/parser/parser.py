#!/usr/bin/env python

# imports
from src.core.util.todo import Todo
from src.core.parser.parserfactory import ParserFactory

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
        factory = ParserFactory()
        for language in self.__code_files:
            try:
                parser = factory.get_parser(language)
            except Exception as ex:
                continue
            for filepath in self.__code_files[language]:
                todos_of_file = parser.parse(filepath) # TODO Optimize this line
                if todos_of_file is not None:
                    self.todo_list += todos_of_file
        return self.todo_list