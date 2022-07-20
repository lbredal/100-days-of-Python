# Calculator part 2
# print vs return
# https://www.udemy.com/course/100-days-of-code/learn/lecture/19658812#overview

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multipy(n1, n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multipy,
    "/": divide
}

num1 = int(input("What's the first number?: "))
for operation in operations:
    print(operation)

operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("What's the second number?: "))



first_answer = operations[operation_symbol](num1,num2)


print(f"{num1} {operation_symbol} {num2} = {first_answer}")

# this is the new part for this exercise - chaining functions

second_operation_symbol = input("Pick another operation: ")
num3 = int(input("What's the next number?: "))
second_answer = operations[second_operation_symbol](first_answer,num3)

print(f"{first_answer} {second_operation_symbol} {num3} = {second_answer}")