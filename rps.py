# Rock, paper & scissors game

# Assign the variables:
# rock = 1
# paper = 2
# scissors = 3
#
# Ask the player to choose rock, paper or scissors.
# The computer will randomly choose rock, paper or scissors.
# Compare the two and print the winner.
#
# If the player and the computer choose the same thing, it's a tie.
#
# Keep score of the number of wins and losses.

import random

player_wins = 0
computer_wins = 0

lose = "You lose! \n"
win = "You win! \n"

print("Welcome to Rock, Paper, Scissors! \n")

while True:

    print("Type 'r' for rock, 'p' for paper, or 's' for scissors. \n")

    choice = input()
    if choice == "r":
        player_choice = 1
    elif choice == "p":
        player_choice = 2
    elif choice == "s":
        player_choice = 3
    else:
        print("Invalid input. \n")
        continue
    computer_choice = random.randint(1, 3)

    if player_choice == computer_choice:
        print("It's a tie! \n")
    elif player_choice == 1 and computer_choice == 3:
        print(win)
        player_wins += 1
    elif player_choice == 2 and computer_choice == 1:
        print(win)
        player_wins += 1
    elif player_choice == 3 and computer_choice == 2:
        print(win)
        player_wins += 1
    elif player_choice == 1 and computer_choice == 2:
        print(lose)
        computer_wins += 1
    elif player_choice == 2 and computer_choice == 3:
        print(lose)
        computer_wins += 1
    elif player_choice == 3 and computer_choice == 1:
        print(lose)
        computer_wins += 1

    print(f"Player: {player_wins}")
    print(f"Computer: {computer_wins} \n")

    print("Type 'q' to quit, or anything else to play again. \n")

    answer = input()
    if answer == "q":
        break
    else:
        continue
