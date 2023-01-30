'''
Helpers
'''

import shutil

def centre_print(text):
    column_width, _ = shutil.get_terminal_size()
    lines = text.split("\n")
    for line in lines:
        print(line.center(column_width))