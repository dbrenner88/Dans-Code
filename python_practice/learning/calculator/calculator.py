import calc_art as a
import os

continue_calc = True


def clear_screen():
    _ = os.system('clear')


def add(n1, n2):
    adding = n1 + n2
    return adding


def subtract(n1, n2):
    sub = n1 - n2
    return sub


def multiply(n1, n2):
    mult = n1 * n2
    return mult


def divide(n1, n2):
    divided = n1 / n2
    return divided


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def exit_calculator():
    exitting = input("Would you like to exit the calculator? (Y/N)\n").lower()
    if exitting == "y":
        print("Good Bye!")
        exit(1)


def calculation(math_type, num_1, num_2):
    """Takes in a math operator for addition, subtraction, 
     multiplication or division and two numbers. 
     Then returns the calculation."""
    if math_type in operators:
        math_func = operators[math_type]
        result = math_func(num_1, num_2)
        print(f"{num_1} {math_type} {num_2} = {result}")
        return result
    else:
        print("Invalid Entries")


print(a.logo)


def calculator():
    first_num_ask = float(input("What's is the first number? "))
    for operator in operators:
        print(operator)
    continue_calc = True
    while continue_calc:
        operator_ask = input("What operator would you like? ")
        second_num_ask = float(input("What is the next number? "))

        number = calculation(math_type=operator_ask,
                             num_1=first_num_ask, num_2=second_num_ask)

        cont_calc = input(
            f"Type 'y' to continue calculating with {number} or type 'n' to start a new calculation: ").lower()
        if cont_calc == 'n':
            continue_calc = False
            clear_screen()
            exit_calculator()
            calculator()
        elif cont_calc == 'y':
            first_num_ask = number


calculator()
