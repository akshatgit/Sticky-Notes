from src.core.util.todo import Todo

class HTMLTodoParser:

    def __init__(self):
        self.language = "HTML"

    def parse(self, filename):
        todo_list = list()
        with open(filename) as f:
            lines = f.readlines()
            for i in range(0, len(lines)):
                if "<!--" in lines[i]: # since comment can be after the code as well
                    stripedLine = lines[i][lines[i].find("<!--"):].strip().lower()
                    if "todo" in stripedLine:
                        todo = Todo(todo_header=stripedLine[stripedLine.find("todo")+4:].strip().rstrip("-->"), todo_body=None, file_path=filename, line_no=i+1)
                        todo_list.append(todo)
        if len(todo_list) > 0:
            return todo_list
        else:
            return None