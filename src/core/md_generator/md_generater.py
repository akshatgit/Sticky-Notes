from jinja2 import Template
import os

class MDGenerator:

    def __init__(self, **kwargs):

        self.__todo_list = kwargs.get("todo_list")
        self.__gen_path = kwargs.get("gen_path", "todo.md")

    def generate_todo_md(self):

        template_file = os.path.dirname(os.path.realpath(__file__))
        with open(template_file) as tf:
            md_template = Template(tf.read())

        rendered_todo_md = md_template.render(todo_list=self.__todo_list)

        with open(self.__gen_path, "a") as gf:
            gf.write(rendered_todo_md)
