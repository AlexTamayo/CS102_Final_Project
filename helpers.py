'''
Helpers
'''

import shutil

def terminal_center_print(text):
    column_width, _ = shutil.get_terminal_size()
    lines = text.split("\n")
    for line in lines:
        print(line.center(column_width))


def center_string(string, length, fill_char):
    """
    Centers a string within a given length, using a specified fill character.
    """
    # Calculate how much padding is needed on each side of the string
    padding = length - len(string)
    padding_left = padding // 2
    padding_right = padding - padding_left
    
    # Build the final string by concatenating the fill character, the string, and the fill character
    final_string = fill_char * padding_left + string + fill_char * padding_right

    return final_string


def square_frame(text, width, vertical_empty_lines = 0, vertical_line = "||", horizontal_line = "="):
    final_text = ""
    
    final_text += vertical_line + center_string(horizontal_line, width - 2, horizontal_line) + vertical_line + "\n"
    final_text += "".join([vertical_line + center_string(" ", width - 2, " ") + vertical_line  + "\n" for i in range(vertical_empty_lines)])
    
    lines = text.split("\n")
    final_text += "".join([vertical_line + center_string(line, width - 2, " ") + vertical_line  + "\n" for line in lines])

    final_text += "".join([vertical_line + center_string(" ", width - 2, " ") + vertical_line  + "\n" for i in range(vertical_empty_lines)])
    final_text += vertical_line + center_string(horizontal_line, width - 2, horizontal_line) + vertical_line + "\n"

    return final_text
