from src.core.parser.language_parsers.html import HTMLTodoParser
from src.core.parser.language_parsers.python import PythonTodoParser

class ParserFactory:

    __instance = None
    
    @staticmethod
    def getInstance():
        # Static Access Method
        if ParserFactory.__instance == None:
            ParserFactory()

    def __init__(self):
        if ParserFactory.__instance != None:
            raise Exception("Parser Factory is a singleton class")
        else:
            ParserFactory.__instance = self 


    # This will return the appropriate parser
    def get_parser(self, language):
        if language == "Python":
            return PythonTodoParser()
        elif language == "HTML":
            return HTMLTodoParser()
        else:
            print ("{language} not supported".format(language=language))
            raise ValueError(language)