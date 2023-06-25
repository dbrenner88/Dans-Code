import random
import string


class RandomLetterGen:
    def __init__(self, number):
        self.number = number

    def randomLetters(self):
        return ''.join(random.choice(string.ascii_lowercase)
                       for i in range(self.number)
                       )


class AskForNumber:
    def __init__(self):
        self.number = None
        self.asking = None

# def invalid_func_str(self):
# x = None
# self.invalid_input_str = f"Invalid input. Will quit after {x} tries."
# self.tries = "Tries: "

    def giveNumber(self):
        x = 10
# inv_txt = AskForNumber()
# inv_txt.invalid_func_str()
        for i in range(x):
            try:
                self.number = int(input("Enter a number: "))
                break
            except ValueError:
                print(
                    f"Invalid input. Will quit after {x} tries. Tries: " + f"{i+1}.")
        else:
            print("Exceeded the maximum tries. Bye.")
            exit(1)

    def continueOn(self):
        validInputs = ["yes", "no"]
        x = 5
        for i in range(x):
            try:
                self.asking = input(
                    f"Do you want to create a random list with {self.number} letters? (yes/no): ").lower()
                if self.asking in validInputs:
                    break
                else:
                    raise ValueError
            except ValueError:
                print(
                    f"Invalid input. After 5 tries will exit. Current Tries: {i+1}.")
        else:
            print("Exceeded the max tries. Goodbye.")
            exit(1)

    def ask(self):
        if self.asking == "yes":
            generator = RandomLetterGen(self.number)
            createdLetters = list(generator.randomLetters())
            sorted_letters = sorted(createdLetters)
            print(f"Here is your random list: {sorted_letters}")
            print(f"This is the number of characters: {len(sorted_letters)}.")

            setList = sorted(set(createdLetters))
            print(f"Here is your unique list: {setList}.")
            print(
                f"This is the new number of characters: {len(setList)}.")
        elif self.asking == "no":
            print("All good, have a great day!")
        else:
            print("invalid Input.")


makeAsk = AskForNumber()
makeAsk.giveNumber()
makeAsk.continueOn()
makeAsk.ask()
