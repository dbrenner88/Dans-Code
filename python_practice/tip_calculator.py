print("Welcome to the tip calculator.")
while True:
    try:
        total_bill = float(input("What was the total bill? "))
        if total_bill == round(total_bill, 2):
            break
        else:
            print("Enter in a valid cost.")
    except:
        print("Please enter in a valid number.")

while True:
    try:
        num_people = int(input("How many people to split the bill? "))
        if num_people == int(num_people):
            break
        else:
            print("Enter in a valid number.")
    except:
        print("Please enter in a valid number.")

valid_tip = (10, 12, 15)

while True:
    try:
        percent_tip = int(
            input("What percentage tip would you like to give? 10,12, or 15? "))
        if percent_tip in valid_tip:
            break
        else:
            print("enter in a valid tip")
    except:
        print("enter in a valid integer tip")

percent_tip = percent_tip / 100

total_tip = total_bill * percent_tip
tip_split = total_tip / float(num_people)

print("Total bill is:", f"${total_bill:.2f}")
print("The total tip is:", f"${total_tip:.2f}")
print("Each person should pay:", f"${tip_split:.2f}")
