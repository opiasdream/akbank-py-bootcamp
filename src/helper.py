import os
def clear_terminal():

    try:
        os.system('cls')

    except:
        os.system('clear')