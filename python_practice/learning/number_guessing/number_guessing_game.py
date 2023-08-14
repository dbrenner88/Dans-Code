import random as r
import number_guess_art as art

modes = {
    "easy": 10,
    "hard": 5
}


def set_level():
    valid_inputs = ["easy", "hard"]
    level = ''
    while True:
        try:
            level = input(
                "What level do you want to play (easy or hard)? ").lower()
            if level in valid_inputs:
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid level. Please choose hard or easy.")
    guesses = modes[level]
    return guesses


def check_answer(guess, final_answer, turns):
    if guess < final_answer:
        print(f"That is too low.")
        return turns - 1
    elif guess > final_answer:
        print(f"That is too high.")
        return turns - 1
    else:
        print(f"That is correct! The number is {final_answer}.")


def game():
    print(art.logo)
    print("Welcome to the number guessing game.\nI'm thinking of a number between 1 - 100.")
    number_of_guesses = set_level()
    answer = r.randint(1, 100)
    while number_of_guesses != answer:
        print(
            f"You have {number_of_guesses} attempts remaining to guess the number.")

        while True:
            try:
                guess = int(input("Guess a number: "))
                break
            except ValueError:
                print("Invalid entry. Please enter in a number.")

        number_of_guesses = check_answer(guess, answer, number_of_guesses)
        if number_of_guesses == 0:
            print(
                f"You have run out of guesses. The number was {answer}. You have lost.")
            return
        elif number_of_guesses != answer:
            print("Guess Again.")


game()
