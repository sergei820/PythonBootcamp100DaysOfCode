import pandas

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# 1. Create a dictionary in this format
# {"A": "Alfa", "B": "Bravo"}

def apply_nato_alphabet():
    nato_alphabet_dict = {}
    # WITHOUT PANDAS
    # with open("nato_phonetic_alphabet.csv", 'r') as file:
    #     rows_list = file.readlines()
    #
    # for row in rows_list:
    #     if row.split(',')[0] == 'letter':
    #         continue
    #     result_dict[row.split(',')[0]]=row.split(',')[1].replace('\n','')

    # WITH PANDAS
    my_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")
    for (index, row) in my_data_frame.iterrows():
        nato_alphabet_dict[row.letter] = row.code
    print(nato_alphabet_dict)


    # 2. Create a list of the phonetic code words from a word that the user inputs
    user_input = input("Enter a word: ")

    input_nato_alphabet_applied = []

    for letter in user_input:
        input_nato_alphabet_applied.append(nato_alphabet_dict[letter.upper()])

    print(input_nato_alphabet_applied)

if __name__ == "__main__":
    apply_nato_alphabet()
