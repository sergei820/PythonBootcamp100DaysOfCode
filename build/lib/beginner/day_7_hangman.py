import random

WORDS = ["Apple", "Intel", "Microsoft", "Amd", "IBM"]
guesses = 12


def hangman():
    word_to_guess = random.choice(WORDS).lower()
    word_to_guess_to_replace = word_to_guess
    user_word = "_" * len(word_to_guess)
    print(f"Word to guess: {word_to_guess} DELETE LATER")
    number_of_tries = len(word_to_guess) * 2

    while user_word != word_to_guess and number_of_tries > 0:
        number_of_tries -= 1
        user_letter = input("Guess a letter: ").lower()
        if user_letter in word_to_guess_to_replace:
            letter_index = word_to_guess_to_replace.index(user_letter)
            user_word = replace_letter_by_index(user_word, user_letter, letter_index)
            word_to_guess_to_replace = replace_letter_by_index(word_to_guess_to_replace, "_", letter_index)
            print(f"You guessed the letter: {user_letter}! Your current progress: {user_word}")
        else:
            print("There's no this letter in the word, please, try again")
        print(f"Tries left: {number_of_tries}")

    if user_word != word_to_guess:
        print(f"Sorry, you loose, the word was: {word_to_guess}. You can try again :)")
    else:
        print(f"Congratulations! You won! Your word was: {word_to_guess}")


def replace_letter_by_index(word: str, letter_to_set: str, index: int):
    result_word = word[:index] + letter_to_set + word[index + 1:]
    return result_word


if __name__ == "__main__":
    hangman()
