"""
Docstring for day 12.main

Working demo: https://appbrewery.github.io/python-day12-demo/

ASCII art from this place: https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Guess+The+Number&x=none&v=4&h=4&w=80&we=false
"""
import random
from art import logo
print(logo)


print(f"""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.""")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard':")

num = random.randint(1,100)

number_of_guesses = 10
if (difficulty == 'hard'):
    number_of_guesses = 5

while (number_of_guesses > 0):
    print(f"You have {number_of_guesses} remaining to guess the number")

    guess = int(input("Make a guess: "))
    if guess == num:
        print(f"You guessed the correct number ({num})!")
        break
    elif guess < num:
        print(f"Too low.")
    else:
        print(f"Too high.")

     
    print(f"Guess again.")
    number_of_guesses -= 1