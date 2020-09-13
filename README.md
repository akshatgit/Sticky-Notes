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

Create a virtualenv:

```shell
python -m venv venv
```

Install requirements:

```shell
pip install -r requirments.txt
```

Activate Vitual ENV:

```shell
source venv/bin/activate
```

Export python path at the root of the structure:

```shell
 export PYTHONPATH='.'
```
