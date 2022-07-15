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

r = 1
p = 2
s = 3

player_wins = 0
computer_wins = 0

print("Welcome to Rock, Paper, Scissors!")
print("Type 'r' for rock, 'p' for paper, or 's' for scissors.")
choice = input()