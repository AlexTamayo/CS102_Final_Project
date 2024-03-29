"""
This is the main program script.

Resources:
https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
"""

from helpers import (
    terminal_center_print,
    square_frame,
    words_grid,
    add_to_string,
    is_alpha_and_space,
)
from ANSI import ANSI
from nintendo_switch_games_list import my_games_list, list_maker
from Trie import Trie
import time
import re


def intro():
    """
    INTRO GRAPHIC
    """
    print
    intro_text = """
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
  """

    print("\n\n")

    print(ANSI.RED)

    intro_b = square_frame(intro_text, 65, 0, ("||"), ("="))
    terminal_center_print(intro_b)

    print(ANSI.END)

    """
  DESCRIPTOR
  """
    print(ANSI.BOLD)
    terminal_center_print("This is Alex's games chooser.")
    print(ANSI.END)

    print("\n")


class Game_Chooser:
    def __init__(self):
        self._game_category_list = Trie()
        for category in list_maker()[0]:
            self._game_category_list.insert(category.lower())

    def start(self):
        intro()
        self._begin()

    def _begin(self):
        """
        This is now set
        """
        question = "What type of game would you like to search for?\n"
        prompt_game_type = "Type a game category and I'll tell you which games are available in Alex's library of that type. You could also enter the number \"1\" to see all available types. "
        invalid_type = "You have entered an invalid character. Only alphabetical characters and the number 1 is accepted."
        game_not_in_list = "Sorry, no game in the list has got those beginning letters. Please try again."
        print(question)
        user_input = input(prompt_game_type)

        if user_input == "1":
            print_list_of_game_type()
            self._begin()

        elif re.match("^[a-zA-Z\s_-]+$", user_input):
            try:
                result = self._search(user_input)
            except IndexError:
                print(game_not_in_list)
                self._begin()

            if isinstance(result, list):
                self._multiple_options(result)
            elif isinstance(result, str):
                self._one_options(result)

        else:
            print(invalid_type)
            self._begin()

    def _multiple_options(self, list):
        prompt_2_text = f"With those beginning letters, your choices are {ANSI.YELLOW}{list}{ANSI.END}."
        print("\n")
        print(prompt_2_text)
        self._begin()

    def _one_options(self, game):
        prompt_3_text = f"The only option with those beginning letters is {ANSI.YELLOW}{game}{ANSI.END}. Do you want to look at {game} games? Enter '{ANSI.BROWN}y{ANSI.END}' for yes or '{ANSI.BROWN}n{ANSI.END}' for no. "
        prompt_3_a_text = f"You have entered an invalid character. Only '{ANSI.BROWN}y{ANSI.END}' or '{ANSI.BROWN}n{ANSI.END}' are accepted."
        print("\n")

        prompt_3_input = input(prompt_3_text)

        if prompt_3_input.isalpha():
            if prompt_3_input.lower() == "y":
                print("\n")
                print_games_selection(game)
                print("\n")
                self._prompt_4(game)
            elif prompt_3_input.lower() == "n":
                self._begin()
            else:
                print("\n")
                print(prompt_3_a_text)
                self._one_options(game)

    def _prompt_4(self, game):
        prompt_4_text = f"Do you want to find other games? Enter '{ANSI.BROWN}y{ANSI.END}' for yes or '{ANSI.BROWN}n{ANSI.END}' for no. "
        prompt_4_a_text = f"You have entered an invalid character. Only '{ANSI.BROWN}y{ANSI.END}' or '{ANSI.BROWN}n{ANSI.END}' are accepted."

        print("\n")

        prompt_4_input = input(prompt_4_text)

        if prompt_4_input.isalpha():
            if prompt_4_input.lower() == "y":
                self._begin()
            elif prompt_4_input.lower() == "n":
                exit()
            else:
                print("\n")
                print(prompt_4_a_text)
                self._one_options(game)

    def _search(self, search_word):
        """
        Returns an item or a list of items based on the input by the user.
        """

        # Search for the word in the Trie
        result = self._game_category_list.search(search_word.lower())

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


def print_list_of_game_type():
    """
    LIST OF AVAILABLE GAME GENRES
    """
    terminal_center_print("[Genres]")
    genre_a = list_maker()[1]
    genre_b = words_grid(genre_a, 2, True, 4)
    genre_c = square_frame(genre_b, 55, 0, "||", "=")
    terminal_center_print(genre_c)
    print("\n")

    """
    LIST OF AVAILABLE MULTIPLAYER TYPES
    """
    multi_a = list_maker()[2]
    multi_b = words_grid(multi_a, 2, True, 2)
    multi_c = square_frame(multi_b, 35, 0, "||", "=")
    terminal_center_print("[Multiplayer Modes]")
    terminal_center_print(multi_c)


def print_games_selection(category_from_autocomplete, format=2):
    def game_return_presentation(game, text_effects=False):
        """
        Function to format and return information about a game
        """
        # List of fields to be displayed for the game
        fields = [
            ("Name:", game.name),
            ("Publisher(s):", add_to_string(game.publisher, ", ")),
            ("Developer(s):", add_to_string(game.developer, ", ")),
            ("Release Date:", game.NA_release_date()),
            ("Categories:", words_grid(game.type_of_game()[0], 2, True, 1, "<")),
        ]

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

    games_by_category_result = games_by_category(category_from_autocomplete)

    # print(f'You selected the category {ANSI.YELLOW}{ANSI.UNDERLINE}{category_from_autocomplete}{ANSI.END}.\n')
    # print(f'Here are all the games in that category:\n')
    # print(category_from_autocomplete)
    # print("\n")

    if games_by_category_result is not None:
        for game in games_by_category_result:
            if format == 1:  # No style with square
                a = game_return_presentation(game)
                b = square_frame(a, 60, 0, ">", ">")
                print(b)

            elif format == 2:  # With style and no square
                a = game_return_presentation(game, True)
                print(a)
                print("\n")
                time.sleep(0.6)

            elif format == 3:  # With style and with square
                a = game_return_presentation(game, True)
                b = square_frame(a, 60, 0, ">", ">")
                print(b)


def games_by_category(result):
    """
    TRIE OF GAME CATEGORY
    """
    # Initialize an empty dictionary to store categories and corresponding games
    category_dict = {}

    # Loop through each game in my_games_list
    for game in my_games_list:
        # Loop through each category of a game
        for category in game.type_of_game()[0]:
            # Check if the lowercase category name is not already in the dictionary
            if category.lower() not in category_dict:
                # If not, add the category as a key and set its value as a list with the game
                category_dict[category.lower()] = [game]

            # If the lowercase category name is already in the dictionary
            elif category.lower() in category_dict:
                # Append the game to the value list of that category key
                category_dict[category.lower()].append(game)
    """
    Check if the input "category" is a string
    """
    # Check if category is a string
    if isinstance(result, str):
        # Check if the lowercase version of "category" exists in "category_dict"
        if result.lower() in category_dict:
            # Return the value of the lowercase "category" key in "category_dict"
            return category_dict[result.lower()]


if __name__ == "__main__":
    a = Game_Chooser()
    a.start()
