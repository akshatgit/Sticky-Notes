from jinja2 import Template
from src.core.util.todo import Todo
import os

class MDGenerator:

    def __init__(self, **kwargs):

        # list of Todo objects
        self.__todo_list = kwargs.get("todo_list")

        # Path along with name of the md file
        # if nothing is mentioned then default is "todo.md in the same folder"
        self.__gen_path = kwargs.get("gen_path", "todo.md")

    def generate_todo_md(self):

        # get the template file dir path - this is the dir of this file
        template_file_dir = os.path.dirname(os.path.realpath(__file__))
        template_file = os.path.join(template_file_dir, "todo.md.template")

        # Read the template content
        with open(template_file) as tf:
            md_template = Template(tf.read())

        # Render the template using Jinja2
        rendered_todo_md = md_template.render(todo_list=self.__todo_list, t=self.__todo_list[0])

        # Create the "md" file
        with open(self.__gen_path, "w") as gf:
            gf.write(rendered_todo_md)

# for testing
if __name__ == "__main__":

    todo_list = []
    todo_list.append(
        Todo(todo_header="test", todo_body="kjashdakhdahdkjhaskda", class_name="class1", file_path="/dkfj/ksjdk", line_no="20", language="python")
    )
    todo_list.append(
        Todo(todo_header="test2", todo_body="osjdisdj", file_path="/skjd/losk", line_no="11")
    )

    todo_list.append(
        Todo(todo_header="test2", todo_body="osjdisdj", file_path="/skjd/losk", line_no="11", language="java")
    )

    m = MDGenerator(todo_list=todo_list)
    m.generate_todo_md()
