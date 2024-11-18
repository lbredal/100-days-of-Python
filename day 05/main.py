# Exercise 1
# Average Height
# https://app.codingrooms.com/w/rJXRNWGD1dph

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#Write your code below this row 👇

number_of_students = 0 
height_of_students = 0

for student in student_heights:
    number_of_students += 1
    height_of_students += student

print(round(height_of_students / number_of_students))


# Exercise 2
# High Score
# https://app.codingrooms.com/w/AKpv6hnhKamD

# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# student_scores = [78, 65, 89, 86, 55, 91, 64, 89]

highest_score = 0

for score in student_scores:
  if score > highest_score:
      highest_score = score

print(f"The highest score in the class is: {highest_score}")

# Exercise 3
# Adding Even Numbers
# https://app.codingrooms.com/w/bvU1AIWajaBR

#Write your code below this row 👇

total = 0

for n in range(0,101,2):
    total += n

print(total)

# Exercise 4
# FizzBuzz
# https://app.codingrooms.com/w/o8GZnhYB5pga
#Write your code below this row 👇

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)


# Day Project
# Password Generator

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = ""

for letter in range(0,nr_letters):
  password += letters[random.randint(0,len(letters)-1)]

for symbol in range(0,nr_symbols):
  password += symbols[random.randint(0,len(symbols)-1)]

for number in range(0,nr_numbers):
  password += numbers[random.randint(0,len(numbers)-1)]

print(password)


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
#print(password.split(""))

password = list(password)

print(password)

random.shuffle(password)

hard_password = ""

for char in password:
  hard_password += char

print(hard_password)





