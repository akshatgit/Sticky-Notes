# setup.py
from setuptools import setup
import setuptools
import shutil
import os

def readme():
    return "StickyNotes"

def get_dependencies():
  with open("requirements.txt") as req:
    lines = req.readlines()
    lines = [line.strip() for line in lines]
    return lines

setup(name='stickynotes',
      version='0.0.1',
      description='Tool to track, extract and generate mark down files from Todos present in code repositories.',
      long_description=readme(),
      classifiers=[
        'Development Status :: 0.0.1',
        'License :: Apache License 2.0',
        'Programming Language :: Python :: 3.5',
        'Automation :: Documentation :: VCS',
      ],
      keywords='Automation Documentation VCS',
      url='https://github.com/akshatgit/Sticky-Notes',
      author='Akshat Sinha, Deepjyoti Mondal, Harsh',
      license='Apache License 2.0',
      packages=setuptools.find_packages(),
      install_requires=get_dependencies(),
      entry_points={
          'console_scripts': ['stickynotes=src.driver.driver:drive'],
      },
      include_package_data=True,
      zip_safe=False)
