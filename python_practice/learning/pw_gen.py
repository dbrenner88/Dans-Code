import random as r
import string as s

letters = list(s.ascii_letters)
numbers = list(s.digits)
symbols = list(s.punctuation)
password = []

print("Welcome to the random password Generator! Please add in your request below.")
letters_req = int(input("How many letters would you like in your password? "))
numbers_req = int(input("How many numbers would you like in your password? "))
symbols_req = int(input("How many symbols would you like in your password? "))

for i in range(1, letters_req + 1):
    password.append(r.choice(letters))
for i in range(1, numbers_req + 1):
    password.append(r.choice(numbers))
for i in range(1, symbols_req + 1):
    password.append(r.choice(symbols))

r.shuffle(password)

new_pw = ''.join(password)

print(f"Here is your new password: {new_pw}")
