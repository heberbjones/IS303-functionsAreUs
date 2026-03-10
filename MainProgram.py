# Heber Jones, Tyler Vanderwood, Jake Gardanier, Carl Ripplinger
"""
Main program to call functions for the game.
"""

import function1_display_intro
import function2_display_menu
import function3_choose_teams
import function4_play_the_game
import function5_display_record  # FIX: This import was missing

# Default team names used until the user picks teams via menu option 1
lstTeamNames = ["Home Team", "Away Team"]

sPlayerName = function1_display_intro.display_intro()
print(f"\nWelcome, {sPlayerName}!")

iWinCount = 0
iLossCount = 0

choice = 0
while choice != 4:

    choice = function2_display_menu.display_menu()

    if choice == 1:
        # FIX: Results were not being saved before — now both team picks are stored in lstTeamNames
        sHomeTeam = function3_choose_teams.choose_team()
        print(f"You chose: {sHomeTeam}")
        sAwayTeam = function3_choose_teams.choose_team(sHomeTeam)
        print(f"Opponent: {sAwayTeam}")
        lstTeamNames = [sHomeTeam, sAwayTeam]

    elif choice == 2:
        # Play the game and track wins/losses
        if function4_play_the_game.play_game(lstTeamNames) == "W":
            iWinCount += 1
        else:
            iLossCount += 1

    elif choice == 3:
        # FIX: display_record was called with no arguments and wasn't imported before
        function5_display_record.display_record(lstTeamNames[0], iWinCount, iLossCount)

    elif choice == 4:
        # FIX: Removed dead 'elif choice == 5' block that could never be reached
        print(f"\nThanks for playing, {sPlayerName}! Final record: {iWinCount}W - {iLossCount}L. Goodbye!")
