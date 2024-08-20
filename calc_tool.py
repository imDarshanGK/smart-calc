print("Welcome to the Python Calculator!")
print("You can perform addition (+), subtraction (-), multiplication (*), and division (/).")

import os
def addition(a,b):
    return a+b
def subtraction(a,b):
    return a-b
def multiplication(a,b):
    return a*b
def division(a,b):
    return a/b

operations_dict = {
    "+":addition,
    "-":subtraction,
    "*":multiplication,
    "/":division
}

def calculator():
    number1 = float(input("Enter first number: "))
    for symbol in operations_dict:
        print(symbol)
    continue_flag = True
    while continue_flag:
        op_symbol = input("Pick an operation: ")
        number2 = float(input("Enter next number: "))
        calulator_function = operations_dict[op_symbol]
        output = calulator_function(number1,number2)
        print(f"{number1} {op_symbol} {number2} = {output}")

        should_continue = input(f"Enter 'y' to continue calculation with {output} or 'n' to start a new calculation or 'x' to exit: ").lower()
        if should_continue == 'y':
            number1 = output
        elif should_continue == 'n':
            continue_flag = False
            os.system("cls")
            calculator()
        else:
            continue_flag = False
            print("Bye")
calculator()
