'''
This is the main program script.

Resources:
https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20
'''

from helpers import centre_print
from ANSI import ANSI


centre_print(f'''

||==========================================================||
||                                                          ||
||                ▄▄▄  ▄▄   ▄▄▄  ▐▄  ▄█ ▄▄                  ||
||               ▐█ ▀█ ██   ▀▄ ▀  █▌█▌▀▐█ ▀                 ||
||               ▄█▀▀█ ██   ▐▀▀ ▄  ██  ▄▀▀▀█▄               ||
||               ▐█  ▐▌▐█▌▐▌▐█▄▄▌ ▐█ █▌▐█▄ ▐█               ||
||                ▀  ▀  ▀▀▀  ▀▀▀  ▀▀ ▀▀ ▀▀▀▀                ||
||              ▄▄    ▄▄▄           ▄▄▄   ▄▄                ||
||             ▐█ ▀  ▐█ ▀█  ██ ▐███ ▀▄ ▀ ▐█ ▀               ||
||             ▄█ ▀█▄▄█▀▀█ ▐█ ▌▐▌▐█ ▐▀▀ ▄▄▀▀▀█▄             ||
||             ▐█▄ ▐█▐█  ▐▌██ ██▌▐█▌▐█▄▄▌▐█▄ ▐█             ||
||              ▀▀▀▀  ▀  ▀ ▀▀  ▀ ▀▀▀ ▀▀▀  ▀▀▀▀              ||
||                   (For Nintendo Switch)                  ||
||                                                          ||
||==========================================================||

''')

centre_print('''
This is Alex's games chooser.

''')

a = input("Type a game category and I'll tell you which games are available in Alex's library of that type. You could also enter the number \"1\" to see all available types.\n\n:")

print("\n"+a)