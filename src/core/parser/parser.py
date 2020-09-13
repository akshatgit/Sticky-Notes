#!/usr/bin/env python

# imports
from src.core.util.todo import Todo

# TODO write the below todo in multiline comment
# TODO ideally there should be a common parser class and then subclass for each language for now creating a common one and adding python parser in it

"""
This class contain parser methods for different languages.
TODO convert the class to parserFactoy 
"""
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
        self.todo_list = list()

    def _parse_todo(self):
        for language in self.__code_files:
            try:
                parser = get_parser(language)
            except Exception as ex:
                continue
            for filepath in self.__code_files[language]:
                parsed_todo_content = parser(filepath)
                if parsed_todo_content is not None:
                    self.parsed_todo[language].append(parsed_todo_content)

        return self.parsed_todo

    # This function will transform the old todo list and return new one
    # TODO optimize this function, current version: language -> file -> todolist -> todo
    def get_todo_list(self):
        old_todo_list = self._parse_todo()
        for todo_lang in old_todo_list:
            for todo_file in old_todo_list[todo_lang]:
                for todo_item in todo_file["todo"]:
                    todo = Todo(todo_header=todo_item[1], todo_body=None, file_path=todo_file["filepath"], line_no=todo_item[0])
                    self.todo_list.append(todo)

        return self.todo_list
            

# This should be a different class, will refract code later
def _getTODOPython(filename):
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
        return todoDict
    else:
        return None

# This should be a different class, will refract code later, ignore code repeatition for now
# As we will be adding support of other languages as well
def _getTODOHTML(filename):
    """
    This function extract the to dos for a given file
    This will return the todo in this format 
    {"filepath":"path/to/file.html","todo":[(lineno,message)]}
    """
    # There is one wat I know todo can be added to a html file i.e inside <!--
    # Above line will also be returned by parser #logic :P 
    todoList = list()
    todoDict = dict()
    with open(filename) as f:
        lines = f.readlines()
        for i in range(0,len(lines)):
            if "<!--" in lines[i]: # since comment can be after the code as well
                stripedLine = lines[i][lines[i].find("<!--"):].strip().lower() # Value in find() can be replaced by the character of language used for commenting
                # TODO will modify the logic to adapt variants of todo
                if "todo" in stripedLine:
                    todoList.append( (i+1,stripedLine[stripedLine.find("todo")+4:].strip()) )
    if len(todoList) > 0:
        todoDict["filepath"] = filename
        todoDict["todo"] = todoList
        return todoDict
    else:
        return None

# This will return the appropriate parser
def get_parser(language):
    if language == "Python": 
        return _getTODOPython
    elif language == "HTML":
        return _getTODOHTML
    else:
        print ("Not supported for {language}".format(language=language))
        raise ValueError(language)

# Driver Code to test parser
# def parser_test():
#     filename = "./parser.py"
#     parser_obj = Parser()
#     print(parser_obj.getTODOPython(filename))

# parser_test()

