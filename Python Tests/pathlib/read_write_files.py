#!/usr/bin/env python3

import pathlib

# read line by line
path = pathlib.Path.cwd() / '.pylintrc'
with open(path, mode='r') as fid:
    headers = [line.strip() for line in fid if line.startswith('#')]
print('\n'.join(headers))

# read contents of a file
print(pathlib.Path('.pylintrc').read_text())
