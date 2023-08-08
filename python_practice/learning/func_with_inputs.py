import string as s
'''
def greet():
    print("Hello.")
    print("This is how you dougie.")
    print("Because all I get is money.")


greet()


def greet_with_name(name):
    print(f"Hello {name}!")
    print(f"{name}. This is how you dougie.")


greet_with_name("Dan")

digits = list(s.digits)

digits.remove('0')
digits.remove('1')
print(digits)


def div_numbers(number):
    is_div = []
    for digit in digits:
        if number % int(digit) > 0:
            is_div.append("not divisible")
        elif number == int(digit):
            is_div.append("same digit")
        else:
            is_div.append("divisible")
    if 'divisible' in is_div:
        print("It's a not prime number.")
    else:
        print("It's a prime number")


div_numbers(int(input("What number would you like divided? ")))



def greet_with(name, location):
    print(f"Hello, {name}! I hear you're from {location}.\nNice to meet you!")


greet_with(name=input("What is your name? "),
           location=input("What city do you live in? "))

'''


def round_up(number_float):
    if int(number_float) == number_float:
        number_float = int(number_float)
    else:
        number_float = int(number_float) + 1
    return number_float


def paint_calc(height, width, cover):
    cans_needed = round_up(float((height * width) / int(coverage)))
    print((height * width) / int(coverage))
    type((height * width) / int(coverage))
    print(f"You'll need {cans_needed} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
