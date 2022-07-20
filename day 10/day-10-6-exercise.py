# Calculator part 3
# recursive calculations
# https://www.udemy.com/course/100-days-of-code/learn/lecture/19658822#overview

from art import logo

def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multipy(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {"+": add, "-": subtract, "*": multipy, "/": divide}


def calculate():
    print(logo)
    
    num1 = float(input("What's the first number?: "))
    for operation in operations:
        print(operation)
    should_continue = True

    while (should_continue):
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?: "))

        answer = operations[operation_symbol](num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        if input(
                f"Type 'y' to continue calculating with {answer}, or type 'n' to start a fresh calculation"
        ) == "y":
            num1 = answer
        else:
            should_continue = False
            calculate()


calculate()
