# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# function
def greet():
    print("Du er fin")
    print("Du er artig")
    print("Har du tenkt over det?")

greet()

# function with parameter
def greet_with_name(name):
    print(f"Du er fin, {name}")
    print("Du er artig")
    print("Har du tenkt over det?")

greet_with_name("Lars Martin")

    
# function with multiple parameters
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How is it like in {location}")

greet_with("Angela", "Los Angeles")

# functions with keyword arguments

greet_with(name="Lars fra Mars", location="Mars")

# Day 8.2
# Prime Number Checker
# https://app.codingrooms.com/w/DbJ51i6d3IeX

#Write your code below this line 👇

def prime_checker(number):
    if number > 1:
        b = True
    else:
        b = False
    for i in range(2,number):
        #print(f"number = {number} and i = {i}")
        if number % i == 0: 
            b = False
    if b:
        print("It's a prime number")
    else:
        print("It's not a prime number")
    
#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)


# Day 8 - Caesar Cipher - Encryption