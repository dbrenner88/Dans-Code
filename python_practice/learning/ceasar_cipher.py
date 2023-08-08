alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def ceasar(cipher_text, shift_amt, cipher_direction):
    word_phrase = ''

    if cipher_direction == "decode":
        shift_amt *= -1

    for letter in cipher_text:
        if letter == ' ':
            word_phrase += letter
        else:
            cipher_index = alphabet.index(letter) + shift_amt
            if cipher_index >= len(alphabet):
                word_phrase += alphabet[cipher_index - len(alphabet)]
            else:
                word_phrase += alphabet[cipher_index]

    print(f"The {cipher_direction}d word or phrase is: {word_phrase}")


ceasar(cipher_text=text, shift_amt=shift, cipher_direction=direction)
