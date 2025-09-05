
def start_app():
    # FileNotFoundError
    try:
        file = open("a_file.txt", "r")
        a_dict = {"key": "value"}
        value = a_dict["non_existing_key"]
    except FileNotFoundError:
        print("FileNotFoundError caught")
        file = open("a_file.txt", "w")
        file.write("Something")
    except KeyError as error_message:
        print(f"The key {error_message} doesn't exist")
    else:
        content = file.read()
        print(content)
    finally:
        file.close()
        print("File was closed")
        raise TypeError("This is an error I made up")

    # KeyError
    # a_dict = {"key": "value"}
    # value = a_dict["non_existing_key"]

    # IndexError
    # a_list = ["Alfa", "Bravo", "Charlie"]
    # a_list[4]

    # TypeError
    # print("some text" + 3)

def start_app_2():
    height = float(input("Height: "))
    weight = int(input("Weight: "))

    if height > 3:
        raise ValueError("Human height shouldn't be more than 3 meters")

    bmi = weight / height ** 2
    print(bmi)

def start_exercise_1():
    # Challenge 1
    fruits = ["Apple", "Pear", "Orange"]

    # Catch the exception and make sure the code runs without crashing.
    def make_pie(index):
        try:
            fruit = fruits[index]
            print(fruit + " pie")
        except IndexError:
            print("Fruit pie")

    make_pie(4)

def start_exercise_2():
    facebook_posts = [
        {'Likes': 21, 'Comments': 2},
        {'Likes': 13, 'Comments': 2, 'Shares': 1},
        {'Likes': 33, 'Comments': 8, 'Shares': 3},
        {'Comments': 4, 'Shares': 2},
        {'Comments': 1, 'Shares': 1},
        {'Likes': 19, 'Comments': 3}
    ]

    def count_likes(posts):

        total_likes = 0
        for post in posts:
            try:
                total_likes = total_likes + post['Likes']
            except KeyError:
                pass

        return total_likes

    count_likes(facebook_posts)


if __name__ == "__main__":
    # start_app()
    # start_app_2()
    start_exercise_1()
    start_exercise_2()
