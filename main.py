# Welcome *name* to the *game*!
# Type yes if you want to play, no if you don't.
# If you type yes, you will be asked to enter your name.
# If you type no, you will be asked to exit the game.
# Give description of the game.
# Give description of the rules.
# Initialize the game.
# Ask the player to enter a number.
# If the number is between 1 and 10, tell the player that the number is between 1 and 10.
# The player will guess the number.
# If the player guesses the number, tell the player that he guessed the number.

# Try 

import random

def the_game():
    number = random.randint(1, 10)
    print("Guess the number.\n")
    guess = int(input())
    if guess == number:
        print("You guessed the number!\n")
    else:
        print("You didn't guess the number :(")
        print(f"The number was {number}\n")
        

print("Welcome to the game!\n")
print("Type your name.")
name = input()
print()
print(f"Hello, {name}" +  "!\n")

while True:
    print("Type yes if you want to play, no if you don't. \n")
    answer = input()
    answers = ["y", "yes"]
    print()
    if answer in answers:
        print("Guess a number between 1 and 10.\n")
        the_game()
    else:
        print("Goodbye!")
        exit()


            