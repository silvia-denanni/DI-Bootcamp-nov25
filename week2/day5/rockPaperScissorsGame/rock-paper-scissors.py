from game import Game

def get_user_menu_choice():
    menu_options = ("Play a new game","Show scores", "Quit")

    print("Menu options: ")
    for option in menu_options:
        print(f"{option}")      #show the menu options to the user

    user_input = input("Please enter you option: ")

    if user_input not in menu_options:
        raise ValueError ("Enter only one of the menu options!")
    else:
        return user_input
     
def print_results(results):
    wins = results.get("win", 0)
    losses = results.get("loss", 0)
    draws = results.get("draw", 0)

    print(f" There are {wins} wins, {losses} losses and {draws} draws.")

    print("Thank you for playing!")


def main():
    results = {"win": 0, "loss": 0, "draw": 0}

    while True:
        choice = get_user_menu_choice()          #storing in variable "choice" the function  

        if choice == "Play a new game":
            game1 = Game                         # instantiate the new game
            result = game1.play()                  #storing in variable "result" the game + CALLING THE METHOD ()!!!

            if result == "You win!":
                results["win"] += 1           
            elif result == "You lose!":
                results ["loss"] += 1
            else:
                results ["draw"] += 1

        elif choice == "Show scores":
            print_results(results)
        
        elif choice == "Quit":
            print_results(results)
            print("Goodbye!")
            break




        
                         