import random

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)

    player = None

    while player not in choices:
        player = input("rock, paper or scissors?:").lower()

    if player == computer:
        print("player:", player)
        print("computer:", computer)
        print("Tie!")
    elif player == "rock":
        if computer == "paper":
            print("Computer:",computer)
            print("Player", player)
            print("You Lose!")
        if computer == "scissors":
            print("Computer:",computer)
            print("Player", player)
            print("You win!")
    elif player == "scissors":
        if computer == "rock":
            print("Computer:",computer)
            print("Player", player)
            print("You Lose!")
        if computer == "paper":
            print("Computer:",computer)
            print("Player", player)
            print("You win!")
    elif player == "paper":
        if computer == "scissors":
            print("Computer:",computer)
            print("Player", player)
            print("You Lose!")
        if computer == "rock":
            print("Computer:",computer)
            print("Player", player)
            print("You win!")

    play_again = input("Play again? (y/n):").lower()
    if play_again != "y":
        break
print("Bye!")