# Data Types

# String

print("Hello"[4])

print ("123" + "345")

# Integer

print(123 + 345)

print(123_456_789)

# Float

print(3.14519)

# Boolean

print(True)


# Exercise 1
# Data Types
# https://app.codingrooms.com/w/aS2uv8nXAhs3
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

digit_1 = int(two_digit_number[0])
digit_2 = int(two_digit_number[1])
sum = str(digit_1 + digit_2)

#print(two_digit_number[0] + " + " + two_digit_number[1] + " = " + sum)
print(sum)

# Exercise 2
# BMI Calculator
# https://app.codingrooms.com/w/2hntavyHDeBs

# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

BMI = int(int(weight) / (float(height) * float(height)))

print(BMI)

# Exercise 3
# Life in Weeks
# https://app.codingrooms.com/w/rOWYWMATKD7d

# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

x = (90 * 365) - (int(age) * 365)
y = (90 * 52) - (int(age) * 52)
z = (90 * 12) - (int(age) *  12)

print("You have " + str(x) + " days, " + str(y) + " weeks, and " + str(z) + " months left.")
#  Using f-string instead
print(f"You have {x} days, {y} weeks, and {z} months left.")



# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number % 2 == 1:
    print("This is an odd number.")
else:
    print("This is an even number.")


# Day 2 Project: Tip Calculator

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")

total_bill = float(input("What was the total bill?\n$"))

tip = int(input("How much tip would you like to give? 10, 12 or 15 ?\n"))

pax = int(input("How many people to split the bill?\n"))

pay_per_pax = total_bill * (tip / 100.00 + 1) / pax

print(f"Each person should pay: ${pay_per_pax:.2f}")
