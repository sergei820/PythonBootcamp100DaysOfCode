# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

def start_app():
    data = pandas.read_csv("nato_phonetic_alphabet.csv")
    phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
    print(phonetic_dict)

    word = input("Enter a word: ").upper()
    try:
        output_list = [phonetic_dict[letter] for letter in word]
        print(output_list)
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        start_app()


if __name__ == "__main__":
    start_app()
