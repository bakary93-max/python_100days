from operator import index


def prime_number(number):
    if number == 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            print("It is not a prime number")
            # return False
    print("It is a prime number")
    # return True


# number = int(input("Enter a number please: "))
# prime_number(number)


alphabet = [
        "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
        "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
    ]
description = input("Tape 'encode' to encode or 'decode' to decode : ").lower()


def encrypt(text, shift):
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position + shift
        if new_position > 25:
            new_position = new_position - 26
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded code is {cipher_text}")


def decrypt(text, shift):
    cipher_text = ""
    for letter in text:
        position = alphabet.index(letter)
        new_position = position - shift
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The decoded code is {cipher_text}")


"""if description == 'encode':
    encrypt("bakary", 3)
elif description == 'decode':
    decrypt("edndub",3)
"""


def caesar(text, shift, direction):
    cipher_text = ""
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position - shift if direction == 'encode' else position + shift
            if new_position > 25:
                new_position -= 26
            new_letter = alphabet[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter
    print(f"The {direction}d code is {cipher_text}")
    finish = input("Type yes to encode or decode another message")
    if finish == 'yes':
        caesar('bakary t',3,description)
    return -1


caesar('bakary t',3,description)
caesar('edndub',3,description)