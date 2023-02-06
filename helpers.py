'''
Helpers
'''

import shutil
import math
from ANSI import ANSI

def terminal_center_print(text):
    # Get the terminal width
    column_width, _ = shutil.get_terminal_size()    
    # Split the text into lines
    lines = text.split("\n")    
    # Iterate over the lines and print each one centered within the terminal width
    for line in lines:
        print(line.center(column_width))

def center_string(string, length, fill_char):
    '''
    Centers a string within a given length, using a specified fill character.
    '''
    # Calculate how much padding is needed on each side of the string
    padding = length - len(string)
    padding_left = padding // 2
    padding_right = padding - padding_left
    
    # Build the final string by concatenating the fill character, the string, and the fill character
    final_string = fill_char * padding_left + string + fill_char * padding_right

    return final_string

def square_frame(text, width, vertical_empty_lines = 0, vertical_line = "||", horizontal_line = "="):
    # Create an empty string to store the final text
    final_text = ""    
    # Add the top horizontal line to the final text
    final_text += vertical_line + center_string(horizontal_line, width - 2, horizontal_line) + vertical_line + "\n"    
    # Add the empty vertical lines to the final text
    final_text += "".join([vertical_line + center_string(" ", width - 2, " ") + vertical_line  + "\n" for i in range(vertical_empty_lines)])    
    # Split the input text into separate lines and add each line to the final text
    lines = text.split("\n")
    final_text += "".join([vertical_line + center_string(line, width - 2, " ") + vertical_line  + "\n" for line in lines])
    # Add the empty vertical lines to the final text
    final_text += "".join([vertical_line + center_string(" ", width - 2, " ") + vertical_line  + "\n" for i in range(vertical_empty_lines)])    
    # Add the bottom horizontal line to the final text
    final_text += vertical_line + center_string(horizontal_line, width - 2, horizontal_line) + vertical_line + "\n"

    # Return the final text
    return final_text

def words_grid(words, columns, equal_spacing=False, width=0, alignment = "^"):
    '''
    This function takes in four parameters:
    words - a list of words to be printed in a grid format
    columns - the number of columns in the grid
    equal_spacing - a boolean indicating whether the words should have equal spacing (default False)
    width - the number of spaces to add between words (default 0)
    
    If equal_spacing is True, the length of each word is calculated and used to determine the 
    maximum word length. The format string is then created to center each word in a space 
    with the length of max_word_len + width. The words are then reformatted using this string.
    '''
    lt_decotator = ""
    rt_decotator = ""
    if equal_spacing:
        max_word_len = max(len(word) for word in words)
        format_str = "{:"+alignment+str(max_word_len + width) + "}"
        words = [format_str.format(lt_decotator+word+rt_decotator) for word in words]
    # Calculate the total width of the grid (the total length of all words in a single row)    
    total_width = (max_word_len + width) * columns
    # Calculate the number of words remaining in the last row if the list of words is not evenly divisible by columns
    words_remaining = len(words) % columns
    # Calculate the total number of rows in the grid
    total_rows = math.ceil(len(words) / columns)
    # Initialize an empty string to store the final grid
    # row_str = "\n"
    row_str = ""
    # Loop through the words, creating rows of words with columns number of words in each row
    for i in range(0, len(words), columns):
        # Get the words for the current row
        row = words[i:i + columns]
        # If the last row is not full, calculate the length of the space to center each word
        if (words_remaining != 0) and (i // columns + 1 == total_rows):
            space_length = total_width // len(row)
            # Center each word in the row using the calculated space length
            for word in row:
                row_str += "{:{}{}}".format(word, alignment, space_length)
                # row_str += "{:"+alignment+word ^{}}".format(word, space_length)
            break
        # Add the words in the current row to the final grid string
        row_str += "".join(row)
        # print(f'Number of iteration: {i}\n')
        # print(f'{i} < {width*total_rows} - {columns} - 1 = {(width*total_rows) - columns} {i < (width*total_rows) - columns}\n')        
        if i < (width*total_rows) - columns:
            # Add a newline character to separate each row
            row_str += "\n"
    # Return the final grid string
    return row_str



def add_to_string(elements, separator):
    '''
    This function takes in two arguments: 
      elements: a list of elements that need to be joined 
      separator: the separator string used to join the elements
    '''

    # The join() method is called on the separator string, 
    # which is used to join all elements in the "elements" list. 
    # The result of the join() method is returned from the function.
    return separator.join(elements)




if __name__ == "__main__":
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape"]
    # print_grid(words, 3, True, 2)
    print(words_grid(words, 2, True, 2, "^"))
    print("BlaBlaBlaBlaBla")
    pass
