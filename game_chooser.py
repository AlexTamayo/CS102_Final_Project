'''
This is the main program script.

Resources:
https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
'''

'''
TO DO


-. First make the list of game types when the user inputs 1. Make it so that it shows in a neatly organised grid.

-. After this, start work on the auto complete and the results.

-. Make it presentable

-. 

-. 

-. 

-. 
'''

from helpers import terminal_center_print, center_string, square_frame, words_grid, add_to_string
from ANSI import ANSI
from NintendoSwithGame import NintendoSwitchGame
from nintendo_switch_games_list import my_games_list, list_maker
from Trie import Trie


'''
INTRO GRAPHIC
'''
intro_text = '''
   ▄▄▄  ▄▄   ▄▄▄  ▐▄  ▄█ ▄▄     
  ▐█ ▀█ ██   ▀▄ ▀  █▌█▌▀▐█ ▀    
  ▄█▀▀█ ██   ▐▀▀ ▄  ██  ▄▀▀▀█▄  
  ▐█  ▐▌▐█▌▐▌▐█▄▄▌ ▐█ █▌▐█▄ ▐█  
   ▀  ▀  ▀▀▀  ▀▀▀  ▀▀ ▀▀ ▀▀▀▀   
 ▄▄    ▄▄▄           ▄▄▄   ▄▄   
▐█ ▀  ▐█ ▀█  ██ ▐███ ▀▄ ▀ ▐█ ▀  
▄█ ▀█▄▄█▀▀█ ▐█ ▌▐▌▐█ ▐▀▀ ▄▄▀▀▀█▄
▐█▄ ▐█▐█  ▐▌██ ██▌▐█▌▐█▄▄▌▐█▄ ▐█
 ▀▀▀▀  ▀  ▀ ▀▀  ▀ ▀▀▀ ▀▀▀  ▀▀▀▀ 
 (For Nintendo Switch)
'''

print("\n\n\n\n")

print(ANSI.RED)

intro_b = square_frame(intro_text, 65, 0, ("||"), ("="))
terminal_center_print(intro_b)

print(ANSI.END)


'''
DESCRIPTOR
'''
print(ANSI.BOLD)
terminal_center_print("This is Alex's games chooser.")

print("\n")

'''
FIRST QUESTION
'''
# a = input("Type a game category and I'll tell you which games are available in Alex's library of that type. You could also enter the number \"1\" to see all available types.\n\n_")

print("\n")

# '''
# LIST OF AVAILABLE GAME GENRES
# '''
# terminal_center_print("[Genres]")
# genre_a = list_maker()[1]
# genre_b = words_grid(genre_a, 2, True, 4)
# genre_c = square_frame(genre_b, 55, 0, "||", "=")
# terminal_center_print(genre_c)
# print("\n")


# '''
# LIST OF AVAILABLE MULTIPLAYER TYPES
# '''
# multi_a = list_maker()[2]
# multi_b = words_grid(multi_a, 2, True, 2)
# multi_c = square_frame(multi_b, 35, 0, "||", "=")
# terminal_center_print("[Multiplayer Modes]")
# terminal_center_print(multi_c)




'''
TRIE OF GAME CATEGORY
'''
category_dict = {}

for game in my_games_list:
  for category in game.type_of_game()[0]:
    if category.lower() not in category_dict:
      category_dict[category.lower()] = [game]
    elif category.lower() in category_dict:
      category_dict[category.lower()].append(game)


# for key, value in category_dict.items():
#   print(f"{key}: {value}")
#   print("\n")



def game_category_autocomplete(search_word):
  '''
  Returns an item or a list of items based on the input by the user.
  '''  
  # Create a Trie data structure to store the game categories
  game_category_list = Trie()
  
  # Add each category to the Trie
  for category in list_maker()[0]:
    game_category_list.insert(category.lower())

  # Search for the word in the Trie
  result = game_category_list.search(search_word.lower())

  # If many results have the same input word, it returns the exact word that was input
  if isinstance(result, list):    
    if len(result) > 1:      
      for category in result:
        if category == search_word.lower():
          result = search_word.title()

  # If there's only one result, return it as a string.
  if len(result) < 2:
    result = result[0].title()

  # Return the result
  return result

def games_by_category(category):
  '''
  Check if the input "category" is a string
  '''  
  # Check if category is a string
  if isinstance(category, str):    
    # Check if the lowercase version of "category" exists in "category_dict"
    if category.lower() in category_dict:      
      # Return the value of the lowercase "category" key in "category_dict"
      return category_dict[category.lower()]


def game_return_presentation(game, text_effects = False):
  '''
  Function to format and return information about a game
  '''
  # List of fields to be displayed for the game
  fields = [("Name:", game.name),
            ("Publisher(s):", add_to_string(game.publisher, ', ')),
            ("Developer(s):", add_to_string(game.developer, ', ')),
            ("Release Date:", game.NA_release_date()),
            ("Categories:", words_grid(game.type_of_game()[0], 2, True, 1, "<"))]
  
  # Initialize an empty string for the presentation text
  presentation_text = ""
  
  # Iterate through each field
  for i, field in enumerate(fields):
    # If text effects are enabled, add ANSI escape codes to format the text
    if text_effects:
      if i < len(fields) - 1:
        presentation_text += f"{ANSI.UNDERLINE}{field[0]}{ANSI.END} {ANSI.RED + ANSI.BOLD}{field[1]}{ANSI.END}"
        presentation_text += "\n"
      # Add a newline between each field, unless it's the last field
      if i == len(fields) - 1:
        presentation_text += f"{ANSI.UNDERLINE}{field[0]}{ANSI.END}\n{ANSI.RED + ANSI.BOLD}{field[1]}{ANSI.END}"
    # If text effects are not enabled, format the text without special formatting
    else:
      presentation_text += f"{field[0]}\n{field[1]}"
      # Add a newline between each field, unless it's the last field
      if i < len(fields) - 1:
        presentation_text += "\n\n"

  # Return the formatted presentation text
  return presentation_text


def print_games_selection(search_input):

  category_from_autocomplete = game_category_autocomplete(search_input)
  games_by_category_result = games_by_category(category_from_autocomplete)

  print(f'You selected the category {ANSI.YELLOW}{ANSI.UNDERLINE}{category_from_autocomplete}{ANSI.END}.\n')
  print(f'Here are all the games in that category:\n')
  # print(category_from_autocomplete)
  # print("\n")


  square_test = 2

  if games_by_category_result is not None:
    for game in games_by_category_result:

      if square_test == 1: # No style with square
        a = game_return_presentation(game)
        b = square_frame(a, 60, 0, ">", ">")
        print(b)

      elif square_test == 2: # With style and no square
        a = game_return_presentation(game, True)
        print(a)
        # print("\n")

      elif square_test == 3: # With style and with square
        a = game_return_presentation(game, True)
        b = square_frame(a, 60, 0, ">", ">")
        print(b)

# print_games_selection("acti")

print(ANSI.END)