import os
import blind_auction_art as a


def clear_screen():
    _ = os.system('clear')


end_program = False
yes_no_validator = ['yes', 'no']
bids = {}


def calculate_winner(dict):
    winning_bid = 0
    winning_name = []

    for val in dict:
        if int(dict[val]) >= winning_bid:
            winning_bid = int(dict[val])

            if int(dict[val]) == winning_bid:
                winning_name.append(val)
            else:
                winning_name = val

            winning_name_string = ''
            for name in winning_name:
                if winning_name_string == '':
                    winning_name_string = name
                else:
                    winning_name_string += ' and ' + name
    print(
        f"Th winning_bid is ${winning_bid}. Congrats {winning_name_string}, you won!")


print(a.logo)
print("\nWelcome to the silent auction! Please Enter your name and bid below:\n")

while end_program is False:

    name = input("What is your name?\n")
    bid = input("What is your bid? (in dollars)\n")

    bids[name] = bid

    more_bidders = input("Are there any more bidders? (Yes or No)\n").lower()

    if more_bidders == "no":
        end_program = True
        calculate_winner(bids)
        print("Good Bye!")
    elif more_bidders == "yes":
        print(clear_screen())
