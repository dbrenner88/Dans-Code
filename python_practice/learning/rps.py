import random as r

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock, paper, scissors]

human_choice = int(input("You are playing Rock, Paper, Scissors against the computer.\n Rock beats Scissors.\n Scissors beats Paper.\n And Paper beats Rock.\n Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

if 0 < human_choice > 2:
    print("This is an invalid entry. Please only select 0, 1 or 2.")
else:
    print(rps[human_choice])

    comp_choice = r.randint(0, 2)
    print(f"Computer Chose:\n" + rps[comp_choice])

    if human_choice == comp_choice:
        print("It's a tie.")
    elif (human_choice == 0 and comp_choice == 2) or (human_choice == 2 and comp_choice == 1) or (human_choice == 1 and comp_choice == 0):
        print("You win!")
    else:
        print("Computer won.")
