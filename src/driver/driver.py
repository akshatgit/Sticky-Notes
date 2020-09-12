'''
    This is the entry point of the app
'''

import optparse

from src.core.crawler.crawler import Crawler
from src.core.md_generator.md_generator import MDGenerator

def drive():

    # commandline option parser
    parser = optparse.OptionParser()
    parser.add_option("-d", "--dir", default=".", dest="dir", type="string", help="path to repo to scan | default is current directory")
    parser.add_option("-o", "--out", dest="out", type="string", help="path to generate the todo md file along with name | default is todo.md in current directory")

    (options, args) = parser.parse_args()

    print ("Generating Mark down file...")

    crawler = Crawler(directory=options.dir)

    # get the crawled code files
    code_files_dict = crawler.getAllCodeFiles()

    # get the list of todos from the parser
    # Use md generator to generate the todo md file

    # example call to generator
    # todo_list is list of Todo's from parser
    # md_generator = MDGenerator(todo_list=todo_list, gen_path=options.out)

# for local testing
if __name__ == "__main__":
    drive()
