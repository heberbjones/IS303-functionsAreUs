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
import function5_display_record

# For function 4 to work there has to be a default team name. 
# Function 3 should return a list that replaces this list. - Heber
lstTeamNames = ["Home Team", "Away Team"]

sPlayerName = function1_display_intro.display_intro()

iWinCount = 0
iLossCount = 0

#calling function2_display_menu and running it inside a loop
choice = 0
while choice != 3:

    choice = function2_display_menu.display_menu()

    if choice == 1:
        lstTeamNames = function3_choose_teams.choose_team()

    elif choice == 2:
        # When function 4 is run, it returns a W or L and updates the
        # W/L count variables for function 5 to use
        if function4_play_the_game.play_game(lstTeamNames) == "W" :
           iWinCount += 1
        else :
           iLossCount += 1

    elif choice == 3:
        function5_display_record.display_record(iWinCount, iLossCount)
        
    elif choice == 4 :
        print("Goodbye!")
