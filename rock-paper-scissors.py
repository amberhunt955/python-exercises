
#& ===== ROCK PAPER SCISSORS =====
import random

#* Define the get_choices function
def get_choices():
    # Ask the player to choose a choice (a move)
    player_move = input("Enter your move (rock, paper, scissors: ")
    # Assign a random move to the computer
    options = ["rock", "paper", "scissors"]
    computer_move = random.choice(options)
    # Dictionaries: used to store data values in key value pairs
    choices = {"player": player_move, "computer": computer_move}
    return choices

#* Save get_choices() result to a variable
choices = get_choices()

#* Create function to check who won
def checkWin(player, computer):
    # string concatenation - f strings include variables within the string
    print(f"You chose {player}, computer chose {computer}.")
    # f string is easier
    if player == computer:
        return "It's a tie!"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win!"
        else:
            return "Paper covers rock! You lose."
    elif player == "paper":
        if computer == "rock":
            return "Paper covers rock! You win!"
        else:
            return "Scissors cut paper! You lose."
    elif player == "scissors":
        if computer == "paper":
            return "Scissors cut paper! You win!"
        else:
            return "Rock smashes scissors! You lose."

##* Call checkWin to find result and print
result = checkWin(choices["player"], choices["computer"])
print(result)