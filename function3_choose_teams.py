# Jake Gardanier
### 3. Display list of all teams and allow the user to 
### choose a team using a menu. Call the function again 
### to let the user choose the opponent but do not 
### display the team they chose previously. Remove that 
### team from the list. Allow the user to select an 
### opponent, and return team name. This function should 
### receive a parameter but give it a default value if 
### none is passed. You can use this function for both 
### choosing the home team and the opponent team.

def choose_team(remove_team=None):

    teams = [
        "BYU",
        "Utah",
        "Stanford",
        "UCLA",
        "USC",
        "Washington"
    ]

    # Remove the home team if selecting opponent
    if remove_team in teams:
        teams.remove(remove_team)

    print("\nChoose a Team:")

    for i in range(len(teams)):
        print(f"{i+1}. {teams[i]}")
        
        choice = int(input("Enter the number of the team: "))
        
        while choice < 1 or choice > len(teams):
            choice = int(input("Invalid choice. Enter a valid number: "))
            selected_team = teams[choice - 1]
            return selected_team