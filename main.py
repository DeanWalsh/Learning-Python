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

import random

def the_game():
    number = random.randint(1, 10)
    print("Guess the number.")
    guess = int(input())
    if guess == number:
        print("You guessed the number!")
    else:
        print("You didn't guess the number :(")
        print("The number was " + str(number))
        
    print("Do you want to play again?")
    answer = input()
    if answer == "yes" or "Yes" or "YES" or "y" or "Y":
        the_game()
    else:
        print("Thanks for playing!")
        exit()

print("Welcome to the game!")
print("Type yes if you want to play, no if you don't.")
answer = input()
if answer == "yes" or "Yes" or "YES" or "y" or "Y":
    print("Type your name.")
    name = input()
    print("Hello, " + name + "!")
    print("I will pick a number between 1 and 10.")
    print("You will have to guess it.")
    print("If you guess the number, I will tell you that you guessed the number.")
    print("If you don't guess the number, I will tell you that you didn't guess the number.")
    the_game()
else:
    print("Goodbye!")
    exit()

            