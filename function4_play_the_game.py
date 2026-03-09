# Heber Jones
"""
4. Play the game receiving both team names. 
Generate random scores without ties. Return W or L.
"""
import random

def play_the_game(sHomeTeam, sAwayTeam):

    while (True) :
        iHomeTeamScore = random.randrange(0,10,1)
        iAwayTeamScore = random.randrange(0,10,1)

        if iHomeTeamScore != iAwayTeamScore :
            break

    if iHomeTeamScore > iAwayTeamScore :
        print(f'{sHomeTeam} beat {sAwayTeam} with {iHomeTeamScore} vs. {iAwayTeamScore}.')
        return "W"
    else :
        print(f'{sAwayTeam} beat {sHomeTeam} with {iHomeTeamScore} vs. {iAwayTeamScore}.')
        return "L"