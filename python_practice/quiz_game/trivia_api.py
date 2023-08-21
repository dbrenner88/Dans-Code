from requests import *

"""
api found here: https://opentdb.com/api_config.php
"""


def user_level(user_selection):
    """Takes in a selection for difficulty and updates the url request to the opentdb api"""
    selection = user_selection
    if selection != 'any':
        return f"&difficulty={selection}"
    else:
        return 0


def pick_level():
    """user enters in the level of difficulty they want to play at"""
    levels = ["easy", "medium", "hard", "any"]
    while True:
        user_lvl = input(
            "What level would you like to play? ('easy'| 'medium' | 'hard' | 'any'): ").lower()
        if user_lvl in levels:
            break
        else:
            print("Invalid Entry.")
    return user_lvl


def fetch_questions(level, cat):
    """fetches 10 random questions from the opentdb.com api"""
    url = "https://opentdb.com/api.php?amount=10&type=boolean"
    if level != 0:
        url += level
    if cat != 0:
        url += cat

    response = get(url)

    if response.status_code == 200:  # 200 OK
        data = response.json()  # Parse JSON response
        if data['response_code'] == 0:
            return data['results']
        elif data['response_code'] == 1:
            return "Code 1: No Results Could not return results. The API doesn't have enough questions for your query. (Ex. Asking for 50 Questions in a Category that only has 20.)"
        elif data['response_code'] == 2:
            return "Code 2: Invalid Parameter Contains an invalid parameter. Arguements passed in aren't valid. (Ex. Amount = Five)"
        elif data['response_code'] == 3:
            return "Code 3: Token Not Found Session Token does not exist."
        elif data['response_code'] == 4:
            return "Code 4: Token Empty Session Token has returned all possible questions for the specified query. Resetting the Token is necessary."
    else:
        return f"API call failed with status code: {response.status_code}"


def fetch_categories():
    categories_url = "https://opentdb.com/api_category.php"
    response_cat = get(categories_url)
    if response_cat.status_code == 200:
        data = response_cat.json()
        return data['trivia_categories']
    else:
        return f"API call failed with status code: {response_cat.status_code}"


def select_category(categories_data):
    """takes in the categories data and provides the category id for the api call."""
    categories = ['any']
    categories_dict = {}

    for cat in categories_data:
        cat_nm = cat['name'].lower()
        categories.append(cat_nm)
        categories_dict[cat_nm] = cat['id']

    cat_string = ''
    for cat in categories:
        last_cat = len(categories) - 1
        if cat == categories[last_cat]:
            cat_string += f"{cat.title()}"
        else:
            cat_string += f"{cat.title()} | "

    print(f"\n{cat_string}\n")

    while True:
        cat_wanted = input(
            "Enter in the category you would like from above: ").lower()
        if cat_wanted in categories:
            if cat_wanted == 'any':
                return cat_wanted
            else:
                return categories_dict[cat_wanted]
        else:
            print("Enter in a valid category.")


def user_category(user_cat):
    """Takes in a selection for category and updates the url request to the opentdb api"""
    selection = user_cat
    if selection != 'any':
        return f"&category={selection}"
    else:
        return 0
