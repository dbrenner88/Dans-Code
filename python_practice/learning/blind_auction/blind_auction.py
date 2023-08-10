import os
import blind_auction_art as a


def clear_screen():
    _ = os.system('clear')


end_program = False
yes_no_validator = ['yes', 'no']
bids = {}
prize = ''


def calculate_winner(dict, auction_prize):
    winning_bid = 0.0
    winning_name = ''

    for val in dict:
        if float(dict[val]) > winning_bid:
            winning_bid = float(dict[val])
            winning_name = val
    print(
        f"The winning_bid is ${winning_bid:.2f}. Congrats {winning_name}, you won the {auction_prize}!\n")


print(a.logo)
print("\nWelcome to the silent auction! Please Enter your name and bid below:\n")
prize = input("What is the prize people are bidding on? ")

while not end_program:
    print(f"\nThe prize you are biding on is {prize}. Good Luck!\n")
    name = input("What is your name?\n")

    bid = float(input("What is your bid? (in dollars)\n$"))

    bids[name] = bid

    more_bidders = ''

    while more_bidders not in (yes_no_validator):
        more_bidders = input(
            "Are there any more bidders? (Yes or No)\n").lower()

        if more_bidders == "no":
            print(clear_screen())
            end_program = True
            calculate_winner(dict=bids, auction_prize=prize)
            print("Good Bye!\n")
        elif more_bidders == "yes":
            print(clear_screen())
