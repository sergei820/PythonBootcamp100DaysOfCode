import random


def play_rock_paper_scissors():
    user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if user_choice != 'n' and (user_choice > 2 or user_choice < 0):
        print("Choose the correct number")
        play_rock_paper_scissors()
    print("You chose: ")
    print(game_images[user_choice])

    computer_choice = random.randint(0,2)
    print("Computer chose: ")
    print(game_images[computer_choice])

    if user_choice == computer_choice:
        print("Draw!")
    elif user_choice == 0:
        if computer_choice == 1:
            print("You lose!")
        if computer_choice == 2:
            print("You win!")
    elif user_choice == 1:
        if computer_choice == 0:
            print("You win!")
        if computer_choice == 2:
            print("You lose!")
    elif user_choice == 2:
        if computer_choice == 0:
            print("You lose!")
        if computer_choice == 1:
            print("You win!")
    play_again = input("Do you want to play again? y/n\n")
    if play_again == "y":
        play_rock_paper_scissors()
    else:
        print("Thank you for playing!")



rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
game_images = [rock, paper, scissors]


if __name__ == '__main__':
    play_rock_paper_scissors()
