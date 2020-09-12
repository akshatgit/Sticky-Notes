# Introduction

Developers are a lazy creature and sometimes while implementing logic in code or modifying configuration we add TO-DO comments to keep a track of missing features. Tracking such TO-DO comments is cumbersome. We plan to structure these comments into meaningful comment blocks and extract them to generate Markdown files. These files can be used to automate different tasks such as slack notification, Git issues, etc.

## Requirements

- python 3.5+ and pip
- Git

## Quickstart

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
