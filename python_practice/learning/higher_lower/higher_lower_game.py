# Game needs to take two different celebrities and display their names, desc, country
# Asks who has more followers
# if user guesses correct, clear screen, add you're right under logo with a count of current score
# bottom celeb moves up to the top and and a new celeb is used to compare against
# wrong screen is cleared game ends and prints Sorry, that's wrong. Final score: [score]

import higher_lower_art as art
import game_data as gd
import random as r
import os


def clear_screen():
    """Clears terminals on mac OS devices"""
    _ = os.system('clear')


celebs = {
    "A": '',
    "B": '',
}


def pick_random():
    """picks a random celebrity from the celebrities list"""
    celebrities = gd.data
    celeb = r.choice(celebrities)
    return celeb


def format_compare(entry):
    """Returns formatted Celebrities based on the celebs dictionary"""
    return f"{entry['name']}, a {entry['description']}, from {entry['country']}"


def check_answer(guess, followers_a, followers_b):
    """Calculates who has more followers between two celebrities when passed in as dictionaries"""
    if followers_a > followers_b:
        return guess == 'A'
    else:
        return guess == 'B'


# select two random celebrities to start the game format: Compare [A/B]: [Name], a [Description], from [country]
celebs['A'] = pick_random()
celebs['B'] = pick_random()
if celebs['B'] == celebs['A']:
    celebs['B'] = pick_random()


def game():
    end_game = False
    score = 0

    while not end_game:
        print(art.logo)
        if score > 0:
            print(f"That was correct! Your score is {score}.")
        print(f"Compare A: {format_compare(celebs['A'])}")
        # add the vs art in between them
        print(art.vs)
        print(f"Compare B: {format_compare(celebs['B'])}")
        # ask the user who has more followers A or B
        user_guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        celeb_a_followers = celebs['A']['follower_count']
        celeb_b_followers = celebs['B']['follower_count']

        is_true = check_answer(
            user_guess, celeb_a_followers, celeb_b_followers)

        if is_true:
            score += 1
            print(f"That was correct! Your score is {score}.")
            celebs['A'] = celebs['B']
            celebs['B'] = pick_random()
            if celebs['A'] == celebs['B']:
                celebs['B'] = pick_random()
            clear_screen()
        else:
            clear_screen()
            end_game = True
            print(f"Sorry, that was incorrect. Your final score is {score}.")


game()
