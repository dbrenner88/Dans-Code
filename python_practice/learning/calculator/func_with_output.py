'''def format_name(f_name, l_name):
    """Take a first and last name and 
    format it to title case."""
    if f_name == '' or l_name == '':
        return print("Valid inputs were not provided")
    formatted_name = f_name.title() + ' ' + l_name.title()
    return formatted_name


dans_name = format_name(input("What is your first name? "),
                        input("What is your last name? "))

print(dans_name)
'''


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
    divided = round(n1 / n2, 2)
    return divided


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def calculation(math_type, num_1, num_2):
    """Takes in a math operator for addition, subtraction, 
     multiplication or division and two numbers. 
     Then returns the calculation."""
    for operator in operators:
        if operator == math_type:
            math = print(operators[operator])
    print(f"{num_1} {math_type} {num_2} = {math}")
    return math


calculation("*", 2, 4)
