# Tyler Vanderwood
"""
2. Display of menu and return choice. Store in 
variable and use this value to determine which 
function to call next.
"""

def display_menu():
    print("\n--Menu--")
    print("1. Choose Teams")
    print("2. Play Game")
    print("3. Exit")
    choice = int(input("Enter your choice (1-3): "))
    return choice