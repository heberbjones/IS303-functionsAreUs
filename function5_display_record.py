# Carl Ripplinger
"""
5. Display the final record for a team. 
Receive the home team data and display information.
"""

# FIX: Function was empty (just 'pass'). Now receives team name and win/loss counts and displays them.
def display_record(sTeamName, iWins, iLosses):
    print("\n--Record--")
    print(f"Team: {sTeamName}")
    print(f"Wins: {iWins}")
    print(f"Losses: {iLosses}")
    iTotalGames = iWins + iLosses
    if iTotalGames > 0:
        fWinPct = iWins / iTotalGames * 100
        print(f"Win Percentage: {fWinPct:.1f}%")
    else:
        print("No games played yet.")