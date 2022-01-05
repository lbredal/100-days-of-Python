# Code produced for day 1 of 100 days

print ("Hello world!")

# Exercise 1 
# Printing 
# https://app.codingrooms.com/w/66KCtNgWU4kX
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")

# Exercise 2
# Debugging Practice
# https://app.codingrooms.com/w/rZ66Nk8s1KXt
print("Day 1 - String Manipulation")
print('String Concatenation is done with the "+" sign.')
print('e.g. print("Hello " + "world")')
print("New lines can be created with a backslash and n.")

# Exercise 3
# Input Function
# https://app.codingrooms.com/w/u6WNvGw27QGv
name = input("What is your name? ")
print(len(name))

# Exercise 4
# Variables
# https://app.codingrooms.com/w/lbbCXeeBQNX7
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

c = a
a = b
b = c


#Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)


# Day 1 Project - Band Name Generator
#1. Create a greeting for your program.
print("Welcome to band name generator 2000")

#2. Ask the user for the city that they grew up in.
city = input("Which city did you grow up in ? \n")

#3. Ask the user for the name of a pet.
pet = input("What is the name of your first pet ? \n")

#4. Combine the name of their city and pet and show them their band name.
bandname = city + " " + pet
print("Your band name is " + bandname)

#5. Make sure the input cursor shows on a new line, see the example at:
#   https://replit.com/@appbrewery/band-name-generator-end