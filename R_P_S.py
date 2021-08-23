#Implementing the rock-paper-scissors game

import random
options = ["rock", "paper", "scissors"]


def mode_1():

    def display_choice(choice):
        random.shuffle(options)
        if choice == 1:
            print(f"You have chosen {options[0]}")
            return options[0]
        elif choice == 2:
            print(f"You have chosen {options[1]}")
            return options[1]
        elif choice == 3:
            print(f"You have chosen {options[2]}")
            return options[2]
        else:
            print("Incorrect input. Try again.")
            mode_1()


    def winner():
        if choice_1 == choice_2:
            return "No winner."
        elif choice_1 == "rock" and choice_2 == "paper":
            return "The computer wins."        
        elif choice_1 == "rock" and choice_2 == "scissors":
            return "You win."
        elif choice_1 == "scissors" and choice_2 == "paper":
            return "You win."        
        elif choice_1 == "scissors" and choice_2 == "rock":
            return "The computer wins." 
        elif choice_1 == "paper" and choice_2 == "rock":
            return "You win."
        elif choice_1 == "paper" and choice_2 == "scissors":
            return "The computer wins." 


    def display_computer_choice(choice):
        if choice == 1:
            print(f"The computer has chosen {options[0]}")
            return options[0]
        elif choice == 2:
            print(f"The computer has chosen {options[1]}")
            return options[1]
        elif choice == 3:
            print(f"The computer has chosen {options[2]}")
            return options[2]
        


    player_1 = input("\nEnter your name: ")
    choice = int(input(f"{player_1}, choose 1, 2 or 3: "))
    choice_1 = display_choice(choice)
    i = [1, 2, 3]
    choice = random.choice(i)
    choice_2 = display_computer_choice(choice)

    print(winner())

    choice = input("Do you want to play again? y/n: ").lower()
    if choice == "y":
        main()
    else:
        quit()


    

def mode_2():

    
    def display_choice(choice):
        random.shuffle(options)
        if choice == 1:
            print(f"You have chosen {options[0]}")
            return options[0]
        elif choice == 2:
            print(f"You have chosen {options[1]}")
            return options[1]
        elif choice == 3:
            print(f"You have chosen {options[2]}")
            return options[2]
        else:
            print("Incorrect input. Try again.")
            quit()
            main()

    def winner():
        if choice_1 == choice_2:
            return "No winner."
        elif choice_1 == "rock" and choice_2 == "paper":
            return f"{player_2} wins."        
        elif choice_1 == "rock" and choice_2 == "scissors":
            return f"{player_1} wins."
        elif choice_1 == "scissors" and choice_2 == "paper":
            return f"{player_1} wins."        
        elif choice_1 == "scissors" and choice_2 == "rock":
            return f"{player_2} wins."
        elif choice_1 == "paper" and choice_2 == "rock":
            return f"{player_1} wins."
        elif choice_1 == "paper" and choice_2 == "scissors":
            return f"{player_2} wins."



    player_1 = input("\nEnter first player's name: ")
    player_2 = input("Enter second player's name: ")
    choice = int(input(f"{player_1}, choose 1, 2 or 3: "))
    choice_1 = display_choice(choice)
    choice = int(input(f"{player_2}, choose 1, 2 or 3: "))
    choice_2 = display_choice(choice)
    print(winner())
    choice = input("Do you want to play again? y/n: ").lower()
    if choice == "y":
        main()
    else:
        quit()

def main():
    print("\nTHE ROCK - PAPER - SCISSORS GAME")
    print("Choose a mode: ")
    print("1. Vs Computer")
    print("2. Vs Human")
    print("Enter 3 to quit.")
    mode = int(input("\n"))
    if mode == 1:
        mode_1()
    elif mode == 2:
        mode_2()
    elif mode == 3:
        quit()
    else:
        main()
main()