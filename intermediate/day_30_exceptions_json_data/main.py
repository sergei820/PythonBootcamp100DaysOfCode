
def start_app():
    # FileNotFoundError
    try:
        file = open("a_file.txt", "r")
        a_dict = {"key": "value"}
        value = a_dict["non_existing_key"]
    except FileNotFoundError:
        file = open("a_file.txt", "w")
        file.write("Something")

    # KeyError
    # a_dict = {"key": "value"}
    # value = a_dict["non_existing_key"]

    # IndexError
    # a_list = ["Alfa", "Bravo", "Charlie"]
    # a_list[4]

    # TypeError
    # print("some text" + 3)


if __name__ == "__main__":
    start_app()