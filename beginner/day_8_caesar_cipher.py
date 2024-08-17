import string
from beginner.utilities.art import caesar_cipher_logo


def caesar():
    alphabet = list(string.ascii_lowercase)

    encode_or_decode = input("Type 'encode' or 'decode': \n").lower()
    original_text = input("Type your message: \n").lower()
    shift = int(input("Type value to shift for: \n"))

    print(alphabet)
    print(caesar_cipher_logo)

    if encode_or_decode == 'decode':
        shift *= -1

    result = ''
    for char in original_text:
        if char in alphabet:
            initial_index = alphabet.index(char)
            result_index = (initial_index + shift) % len(alphabet)
            result += alphabet[result_index]
        else:
            result += char
    print(f"Here's the {encode_or_decode}d result: {result}")

    should_continue = input("Do you want to continue? y/n\n")
    if should_continue == 'y':
        caesar()
    else:
        print("Goodbye!")


if __name__ == '__main__':
    caesar()
