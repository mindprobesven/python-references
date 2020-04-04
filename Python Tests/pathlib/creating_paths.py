#!/usr/bin/env python3

import pathlib

print(pathlib.Path())
# .

# current working diretory
print(pathlib.Path.cwd())
# /Users/svenkohn/Desktop/python-references/Python Tests/pathlib

# user home diretory
print(pathlib.Path.home())
# /Users/svenkohn

# from string
print(pathlib.Path('/usr/bin'))
# /usr/bin
print(pathlib.Path('creating_paths.py'))
# creating_paths.py

# Relative path of this file´s parent directory
print(pathlib.Path(__file__).parent)
# .

# Name of this file
print(pathlib.Path(__file__))
# creating_paths.py

# resolve method will find the fill path
print(pathlib.Path(__file__).resolve())
# /Users/svenkohn/Desktop/python-references/Python Tests/pathlib/creating_paths.py
print(pathlib.Path(__file__).resolve().parent)
# /Users/svenkohn/Desktop/python-references/Python Tests/pathlib
