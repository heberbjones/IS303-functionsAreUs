# Heber Jones, Tyler Vanderwood, Jake Gardanier, Carl Ripplinger
"""
Main program to call functions for the game.
It also does task five in GroupPland.md:

5. Display the final record for a team. 
Receive the home team data and display information.
"""

import function1_display_intro
import function2_display_menu
import function3_choose_teams
import function4_play_the_game

sPlayerName = function1_display_intro.display_intro()

#calling function2_display_menu and running it inside a loop
choice = 0
while choice != 3:
    choice = function2_display_menu.display_menu()
    if choice == 1:
        function3_choose_teams.choose_team()
    elif choice == 2:
        function4_play_the_game.play_game()
    elif choice == 3:
        print("Goodbye!")