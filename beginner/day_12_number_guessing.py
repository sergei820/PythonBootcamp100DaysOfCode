import random

EASY_LEVEL_ATTEMPTS = 8
HARD_LEVEL_ATTEMPTS = 5


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': \n").lower()

    attempts = 0
    if difficulty == "hard":
        attempts = HARD_LEVEL_ATTEMPTS
    elif difficulty == "easy":
        attempts = EASY_LEVEL_ATTEMPTS
    return attempts


def play_number_guessing():

    print("Welcome to the Number Guessing")
    print("I'm thinking of a number between 1 and 100")
    number = random.randint(1, 100)

    attempts = set_difficulty()
    while attempts > 0:
        print(f"You have {attempts} attempts to guess the number")
        guess = int(input("Make a guess\n"))
        attempts -= 1
        if guess == number:
            play_again = input("Congratulations! You won! Would you like to play again? y/n: ")
            if play_again == "y":
                play_number_guessing()
            else:
                print("Thanks for playing!")
                break
            break
        if guess < number:
            print("Too low")
        if guess > number:
            print("Too high")
        if attempts == 0:
            play_again = input("You ran out of attempts. Would you like to play again? y/n: ")
            if play_again == "y":
                play_number_guessing()
            else:
                print("Thanks for playing!")
                break


if __name__ == "__main__":
    play_number_guessing()
