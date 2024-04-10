# Get the last part of a path in Python

import pathlib

path = '/home/borislav/Desktop/last/'

last_part = pathlib.PurePath(path).name
print(last_part)  # 👉️ 'last'