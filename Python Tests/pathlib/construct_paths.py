#!/usr/bin/env python3

import pathlib

# cjoin the parts of the path using the special operator /
print(pathlib.Path.home() / 'python' / 'scripts' / 'test.py')
# /Users/svenkohn/python/scripts/test.py

# joinpath method
print(pathlib.Path.home().joinpath('python', 'scripts', 'test.py'))
# /Users/svenkohn/python/scripts/test.py
