import cipher_art as art
import alphabet as a

print(art.logo)
end_cipher = False
correct_direction = False
correct_shift = False

while end_cipher is False:
    direction_vals = ['encode', 'decode']

    while correct_direction is False:
        direction = input(
            "Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        if direction in direction_vals:
            correct_direction = True
        else:
            print("You entered in an incorrect value. Please try again.\n")
    text = input("Type your message:\n").lower()

    while correct_shift is False:
        try:
            shift = int(input("Type the shift number:\n"))
            a.increase_chars(shift)
            correct_shift = True
        except:
            print("Please enter in a valid integer.\n")

    def ceasar(cipher_text, shift_amt, cipher_direction):
        word_phrase = ''

        if cipher_direction == "decode":
            shift_amt *= -1

        for char in cipher_text:
            cipher_index = a.alphabet_with_chars.index(char) + shift_amt
            word_phrase += a.alphabet_with_chars[cipher_index]

        print(f"The {cipher_direction}d word or phrase is: {word_phrase}")

    ceasar(cipher_text=text, shift_amt=shift, cipher_direction=direction)

    keep_going = input(
        " \nWould you like to encrypt or decrpyt something else?\n(Please enter in Yes or No)\n").lower()
    if keep_going == "yes":
        end_cipher = False
        correct_direction = False
        correct_shift = False

    else:
        print("\nGoodbye!\n")
        end_cipher = True
