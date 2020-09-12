class Todo:

    '''
        Class to hold a Todo extracted from a file
        This class should be used to represent a todo.
    '''

    def __init__(**kwargs):

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

    # TODO : will add getter setter for all

