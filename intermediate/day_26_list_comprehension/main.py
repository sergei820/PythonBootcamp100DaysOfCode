

def start_app():
    my_list = [1, 2, 3]
    new_list = [n + 1 for n in my_list]
    print(new_list)

    range_list = [i * 2 for i in range(1, 5)]
    print(range_list)

    names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
    long_names_upper_case = [name.upper() for name in names if len(name) > 4]
    print(long_names_upper_case)

    # Exercise 1
    numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    squared_numbers = [i * i for i in numbers]
    print(f"Exercise 1: {squared_numbers}")

    # Exercise 2
    list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
    numbers = [int(i) for i in list_of_strings]
    result = [i for i in numbers if i % 2 == 0]
    print(f"Exercise 2: {result}")

    # Exercise 3
    list_1 = []
    list_2 = []

    with open("file1.txt", 'r') as file_1:
        list_1 = file_1.readlines()

    with open("file2.txt", 'r') as file_2:
        list_2 = file_2.readlines()

    result = [int(i.replace('\n', '')) for i in list_1 if i in list_2]

    print(f"Exercise 3: {result}")


if __name__ == "__main__":
    start_app()