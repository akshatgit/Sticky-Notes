# Introduction

Developers are a lazy creature and sometimes while implementing logic in code or modifying configuration we add TO-DO comments to keep a track of missing features. Tracking such TO-DO comments is cumbersome. We plan to structure these comments into meaningful comment blocks and extract them to generate Markdown files. These files can be used to automate different tasks such as slack notification, Git issues, etc.

## Requirements

- python 3.5+ and pip
- Git

## Quickstart

### Installing Sticky-Notes

**Using pip and github**

You can easily install Sticky-Notes from github release using pip using the following steps

```
- Open terminal
- Make sure you have pip3 installed
- Exectute - sudo pip3 install https://github.com/akshatgit/Sticky-Notes/releases/download/v0.0.1/stickynotes-0.0.1.tar.gz
- Above is just an example, you can use whichever release you want, although its better to use the latest release

```

You can also install Sticky-Notes directly from the repo itself, if you want ongoing development code

```
sudo pip3 install git+git://github.com/akshatgit/Sticky-Notes

```

**Installing from source**

You can install Sticky-Notes from the source as follows:

```
- Open terminal
- Clone this repo using git clone or simply download it
- cd Sticky-Notes
- sudo python3 setup.py install
```

Once you have installed Sticky-Notes using one of the above method, verify that its installed using :

```
stickynotes --help

```

## Demo Video
[![asciicast](https://asciinema.org/a/14.png)](https://asciinema.org/a/5xadCuVBnhELxNlHTTzb0ueJZ)


## Sticky-Notes Usage

```
Usage: stickynotes [options]

Options:
  -h, --help         show this help message and exit
  -d DIR, --dir=DIR  path to repo to scan | default is current directory
  -o OUT, --out=OUT  path to generate the todo md file along with name |
                     default is todo.md in current directory
```

You can generate the markdown file for your TODOs by simply invoking stickynotes without any args from within your repo
It will generate a file named ```todo.md``` in the root of your repo.

You can also sepcify the path to your repo and custom path for your todo.md file.

```
stickynotes -d /path/to/your/repo -o /path/to/todo_file_name.md

```

## Cite

- [Language extension](https://gist.github.com/aymen-mouelhi/82c93fbcd25f091f2c13faa5e0d61760) by Aymen Mouelhi