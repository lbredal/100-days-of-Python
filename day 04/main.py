# Exercise 1
# Heads or Tails
# https://app.codingrooms.com/w/QGo2Gv7azc4h
import random
#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
 # 🚨 Don't change the code above 👆 It's only for testing your code.
	 
#Write the rest of your code below this line 👇
import random

random_number = random.randint(0,1)

if random_number == 0:
  print("Tails")
else:
  print("Heads")

# Exercise 2
# Banker Roulette
# https://app.codingrooms.com/w/itYqM52OlEXX

import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#names_string = "Angela, Ben, Jenny, Michael, Chloe"
#names = names_string.split(", ")

payer = names[random.randint(0,len(names)-1)]

print(f"{payer} is going to buy the meal today!")


# Exercise 3
# Treasure Map
# https://app.codingrooms.com/w/AnozMgePRlbt

# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

map[int(position[0])-1][int(position[1])-1] = "X"

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

# Project - Rock Paper Scissors

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

human_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))

computer_choice = random.randint(0,2)

rock_paper_scissors = [rock, paper, scissors]
rock_paper_scissors_text = ["rock", "paper", "scissors"]

print("h00man choice: " + rock_paper_scissors_text[human_choice])
print(rock_paper_scissors[human_choice])

print("computer choice: " + rock_paper_scissors_text[computer_choice])
print(rock_paper_scissors[computer_choice])

if human_choice == computer_choice:
  print("Tie.")
elif human_choice == 0:
  if computer_choice == 1:
    print("You lose.")
  elif computer_choice == 2:
    print("You win")
elif human_choice == 1:
  if computer_choice == 0:
    print("You win")
  elif computer_choice == 2:
    print("You lose.")
elif human_choice == 2:
  if computer_choice == 0:
    print("You lose.")
  elif computer_choice == 1:
    print("You win.")


