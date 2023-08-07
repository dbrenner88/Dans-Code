import random as r
import string as s

letters = list(s.ascii_letters)
numbers = list(s.digits)
symbols = list(s.punctuation)
password = []

requested_char = ['letters', 'numbers', 'symbols']

print("Welcome to the random password Generator! Please add in your request below.")


letters_req = int(input("How many letters would you like in your password? "))
numbers_req = int(input("How many numbers would you like in your password? "))
symbols_req = int(input("How many symbols would you like in your password? "))

'''
def ask_char(requested_char):
    for char_type in requested_char:
        num_char = int(
            input(f"How many {char_type} would you like in your password? "))
        requested_char[char_type] = num_char

print(requested_char)
'''


def append_char(num_char, char):
    while num_char > 0:
        password.append(r.choice(char))
        num_char -= 1


append_char(letters_req, letters)
append_char(numbers_req, numbers)
append_char(symbols_req, symbols)

r.shuffle(password)

new_pw = ''.join(password)

print(f"Here is your new password: {new_pw}")
