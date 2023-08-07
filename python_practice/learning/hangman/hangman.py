import random
import csv
import hangman_art as art
import hangman_words as words

word_list = words.word_list
stages = art.stages
end_of_game = False
lives = 6
guessed_letters = ''

file_path = 'more_words.csv'

extended_word_list = word_list

with open(file_path, newline='') as more_words:
    csv_reader = csv.reader(more_words)
    for row in csv_reader:
        extended_word_list.append(row[0])

chosen_word = random.choice(extended_word_list)
word_length = len(chosen_word)

print(art.logo)

display = []
for _ in range(word_length):
    display += "_"

while end_of_game == False:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(
            f"You already guessed the letter {guess}. Try Again!\nHere are the letters you have guessed already: {guessed_letters}.")
    else:
        for position in range(word_length):
            letter = chosen_word[position]
            if letter == guess:
                display[position] = letter
                guessed_letters = guessed_letters + guess

        if guess not in chosen_word and guess not in guessed_letters:
            lives -= 1
            guessed_letters = guessed_letters + guess
            print(
                f"Wrong Guess. The letter {guess} is not in the word.\nyou lose a life.\nYou have {lives} lives left.")

            if lives == 0:
                print(
                    f"Sorry, you lost. The word was {chosen_word}. \nBetter luck next time!")
                end_of_game = True

    if "_" not in display:
        print("Congrats You Won!")
        end_of_game = True

    print(stages[lives])
    print(f"{' '.join(display)}")
