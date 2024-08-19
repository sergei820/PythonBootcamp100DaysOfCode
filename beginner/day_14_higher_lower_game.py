from utilities.game_data import data
import random
import utilities.art


user_score = 0


def get_entity_from_collection(collection):
    random_unique_index = random.randint(0, len(collection) - 1)
    entity = collection.pop(random_unique_index)
    return entity


def get_entity_description_for_comparison(entity):
    return f"{entity['name']}, a {entity['description']}, from {entity['country']}"


def ask_who_has_more_followers(object1, object2):
    print(utilities.art.higher_lower_logo)
    print(f"Compare A: {get_entity_description_for_comparison(object1)}")
    print(utilities.art.higher_lower_vs)
    print(f"Compare B: {get_entity_description_for_comparison(object2)}")
    return input("Who has more followers? Type 'A' or 'B': ").lower()


def play_higher_lower():
    game_data = data
    print(game_data[0]['name'])

    has_user_guessed = True

    while has_user_guessed:
        print(len(game_data))
        object1 = get_entity_from_collection(game_data)
        object2 = get_entity_from_collection(game_data)
        print(object1)
        print(object2)
        print(len(game_data))

        user_answer = ask_who_has_more_followers(object1, object2)

        if int(object1['follower_count']) > int(object2['follower_count']):
            right_answer = 'a'
        else:
            right_answer = 'b'
        if user_answer == right_answer:
            global user_score
            user_score += 1
            print(f"Correct! Your score is {user_score}")
        else:
            has_user_guessed = False
            play_again = input(f"Sorry, you haven't guessed. Would you like to play again? y/n: ")
            if play_again == 'y':
                play_higher_lower()
            else:
                print("Goodbye!")


if __name__ == '__main__':
    play_higher_lower()
