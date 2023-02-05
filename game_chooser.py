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

# print(ANSI.BOLD)
# print(ANSI.RED)

# terminal_center_print(square_frame(intro_text, 65, 0, ("||"), ("=")))

# print(ANSI.END)


'''
DESCRIPTOR
'''
# print(ANSI.BOLD)
terminal_center_print("This is Alex's games chooser.")

print("\n")

# '''
# FIRST QUESTION
# '''
# a = input("Type a game category and I'll tell you which games are available in Alex's library of that type. You could also enter the number \"1\" to see all available types.\n\n_")

# print("\n")

# '''
# LIST OF AVAILABLE GAME GENRES
# '''
# terminal_center_print("[Genres]")
# terminal_center_print(square_frame(words_grid(list_maker()[1], 2, True, 4), 55, 0, "||", "="))

# print("\n")


# '''
# LIST OF AVAILABLE MULTIPLAYER TYPES
# '''
# terminal_center_print("[Multiplayer Modes]")
# terminal_center_print(square_frame(words_grid(list_maker()[2], 2, True, 2), 35, 0, "||", "="))


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
  # Create a Trie data structure to store the game categories
  game_category_list = Trie()
  
  # Add each category to the Trie
  for category in list_maker()[0]:
    game_category_list.insert(category.lower())

  # Search for the word in the Trie
  result = game_category_list.search(search_word.lower())

  # If many results have the same input word, it returns the exact word that was input
  if len(result) > 1:
    for category in result:
      if category == search_word:
        result = search_word.title()

  # If there's only one result, return it as a string.
  if len(result) < 2:
    result = result[0].title()

  # Return the result
  return result

category_from_autocomplete = game_category_autocomplete("action ")

print(category_from_autocomplete)
print("\n")




def games_by_category(category):

  if isinstance(category, str):
    if category.lower() in category_dict:
      return category_dict[category.lower()]

games_by_category_result = games_by_category(category_from_autocomplete)



'''
GAME RETURN PRESENTATION
'''

def game_return_presentation(game, text_effects = False):

  fields = [("Name:", game.name),
            ("Publisher(s):", add_to_string(game.publisher, ', ')),
            ("Developer(s):", add_to_string(game.developer, ', ')),
            ("Release Date:", game.NA_release_date()),
            ("Categories:", words_grid(game.type_of_game()[0], 2, True, 1, "<"))]

  presentation_text = ""
  for i, field in enumerate(fields):
    if text_effects:
      presentation_text += f"{ANSI.UNDERLINE}{field[0]}{ANSI.END} {ANSI.RED + ANSI.BOLD}{field[1]}{ANSI.END}"
    else:
      presentation_text += f"{field[0]}\n{field[1]}\n\n"
    if i < len(fields) - 0:
      presentation_text += "\n"

  return presentation_text





# list_games = [4, 7, 14, 19, 31]
list_games = []

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

# print(ANSI.END)