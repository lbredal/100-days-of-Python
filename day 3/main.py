# Exercise 1
# Odd or Even ?
# https://app.codingrooms.com/w/6f9QqMS8nNN1

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number % 2 == 1:
    print("This is an odd number.")
else:
    print("This is an even number.")

# Exercise 2
# BMI 2.0
# https://app.codingrooms.com/w/d723jGO65w6j

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = round(weight / height**2)

if (bmi < 18.5):
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi >= 18.5 and bmi < 25:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi >= 25 and bmi < 30:
    print(f"Your BMI is {bmi}, you are slightly overweight .")
elif bmi >= 30 and bmi < 35:
    print(f"Your BMI is {bmi}, you are obese.")
elif bmi > 35:
    print(f"Your BMI is {bmi}, you are clinically obese.")
else:
    print(f"You are just weird") 


# Exercise 3
# Leap Year
# https://app.codingrooms.com/w/YjznpoaBnYtm
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

leap_year = bool(False)

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leap_year = True
        else:
            leap_year = False
    else:
        leap_year = True
else:
    leap_year = False

if leap_year: 
    print("Leap year.")
else:
    print("Not leap year.")
  
# Exercise 4
# Python Pizza
# https://app.codingrooms.com/w/dLfyQmr4GSAI

# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bill = 0

if size == "S":
    bill = 15

    if add_pepperoni == "Y":
        bill += 2

if size == "M":
    bill = 20

    if add_pepperoni == "Y":
        bill += 3
    
if size == "L":
    bill = 25

    if add_pepperoni == "Y":
        bill += 3

if extra_cheese == "Y":
    bill += 1


print(f"Your final bill is: ${bill}")


# Exercise 5
# Love Calculator
# https://app.codingrooms.com/w/DQDEAuxx2yh8

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name = name1.lower() + name2.lower()
true_count = 0
love_count = 0

true_count += name.count("t")
true_count += name.count("r")
true_count += name.count("u")
true_count += name.count("e")
love_count += name.count("l")
love_count += name.count("o")
love_count += name.count("v")
love_count += name.count("e")

score = int(str(true_count) + str(love_count))

if score < 10 or score > 90:
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score > 40 and score < 50:
    print(f"Your score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")


# Day Project
# Treasure Island

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

smell = input('You can smell something weird to the right. Want to walk in that direction ? "Y" or "N"')

if smell == "Y":
  print("You can't stand the stench. Game over.")
else:
  wait = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across.')

  if wait == "wait":
    print("You stand there forever. Game over.")
  else:
    door = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which colour do you choose?")

    if door == "red":
      print("You found the treasure! You win!")
    elif door == "yellow":
      print("It's a room full of fire. Game over.")
    elif door == "blue":
      print("You get attacked by an angry stepmom. Game over.")
    else:
      print("You got lost. Game over.")