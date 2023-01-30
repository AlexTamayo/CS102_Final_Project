'''
This is the main program script.

Resources:
https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
'''

'''
TO DO

-. Look into changing the the type formatting to something that gives me the Single Player and Genre separately
from the multiplayer stuff. So it will basically show up as two list. One of genres and another of the multiplayer options.
I could do this either in the class or in the list maker.

-. First make the list of game types when the user inputs 1. Make it so that it shows in a neatly organised grid.

-. After this, start work on the auto complete and the results.

-. Make it presentable

-. 

-. 

-. 

-. 
'''

from helpers import terminal_center_print, center_string, square_frame
from ANSI import ANSI
from NintendoSwithGame import NintendoSwitchGame
from nintendo_switch_games_list import my_games_list, list_maker



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

terminal_center_print(square_frame(intro_text, 65, 0, "||", "="))

terminal_center_print("This is Alex's games chooser.")

# a = input("Type a game category and I'll tell you which games are available in Alex's library of that type. You could also enter the number \"1\" to see all available types.\n\n:")

# for i in list_maker():
#     print(i)