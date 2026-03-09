# Tyler Vanderwood
"""
2. Display of menu and return choice. Store in 
variable and use this value to determine which 
function to call next.
"""

def display_menu():
    print("\n--Menu--")
    print("1. Choose Teams")
    print("2. Play The Game")
    print("3. Display Record")
    print("4. Exit")
    choice = int(input("Enter your choice (1-4): "))
    return choice