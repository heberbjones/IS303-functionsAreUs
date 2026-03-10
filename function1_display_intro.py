# Heber Jones
"""
1. Display an introduction to the game explaining 
rules and prompt for their name and display that in 
the welcome message. Return the name to the main 
program and store it in variable so it can be used 
throughout the program.
"""

def display_intro():
    print("--Game Intro--")
    print("Here are the game rules:")
    sPlayerName = input("Enter your name to begin: ")
    return sPlayerName

    