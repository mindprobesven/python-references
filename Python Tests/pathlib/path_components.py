#!/usr/bin/env python3

import pathlib

""" .name: the file name without any directory
.parent: the directory containing the file, or the parent directory if path is a directory
.stem: the file name without the suffix
.suffix: the file extension
.anchor: the part of the path before the directories """

path = pathlib.Path(__file__).resolve()
print(path)
# /Users/svenkohn/Desktop/python-references/Python Tests/pathlib/path_components.py
print(path.stem)
# path_components
print(path.suffix)
# .py
print(path.name)
# path_components.py
print(path.anchor)
# /
