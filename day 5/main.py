# Exercise 1
# Average Height
# https://app.codingrooms.com/w/rJXRNWGD1dph

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#Write your code below this row 👇

print(student_heights)
print(sum(student_heights))
print(len(student_heights))

number_of_students = 0 
height_of_students = 0

for student in student_heights:
    number_of_students += 1
    height_of_students += student

print(height_of_students)
print(number_of_students)
print(round(height_of_students / number_of_students))


