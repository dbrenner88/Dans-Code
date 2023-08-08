import math as m
import string as s

alphabet_with_chars = list(s.ascii_lowercase+' ' + s.digits + s.punctuation)
length_of_alphabet_chars = len(alphabet_with_chars)


def increase_chars(char_shift):
    number_of_chars = m.ceil(char_shift / length_of_alphabet_chars)
    for num in range(number_of_chars):
        alphabet_with_chars.extend(alphabet_with_chars)
