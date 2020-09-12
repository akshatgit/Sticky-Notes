from jinja2 import Template

class MDGenerator:

    def __init__(self, **kwargs):
        self.__todo_list = kwargs.get("todo_list")
        self.__gen_path = kwargs.get("gen_path")

    def generate_todo_md(self):
        pass
