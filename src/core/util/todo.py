class Todo:

    '''
        Class to hold a Todo extracted from a file
        This class should be used to represent a todo.
    '''

    def __init__(self, **kwargs):

        self.__todo_header = kwargs.get("todo_header")
        self.__todo_body = kwargs.get("todo_body")
        self.__file_path = kwargs.get("file_path")
        self.__line_no = kwargs.get("line_no")

        # optional
        self.__func_name = kwargs.get("func_name")

        #optional
        self.__class_name = kwargs.get("class_name")

        #optional
        self.__language = kwargs.get("language")

    def set_todo_header(self, todo_header):
        self.__todo_header = todo_header

    def get_todo_header(self):
        return self.__todo_header

    def set_todo_body(self, todo_body):
        self.__set_todo_body = todo_body

    def get_todo_body(self):
        return self.__todo_body

    def set_file_path(self, file_path):
        self.__file_path = file_path

    def get_file_path(self):
        return self.__file_path

    def set_line_no(self, line_no):
        self.__line_no = line_no

    def get_line_no(self):
        return self.__line_no

    def set_func_name(self, func_name):
        self.__func_name = func_name

    def get_func_name(self):
        return self.__func_name

    def set_class_name(self, class_name):
        self.__class_name = class_name

    def get_class_name(self):
        return self.__class_name

    def set_language(self, language):
        self.__language = language

    def get_language(self):
        return self.__language
