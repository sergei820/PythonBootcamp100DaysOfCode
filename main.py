
def start_app(text):
    line1 = ["⬜️", "️⬜️", "️⬜️"]
    line2 = ["⬜️", "⬜️", "️⬜️"]
    line3 = ["⬜️️", "⬜️️", "⬜️️"]
    map = [line1, line2, line3]
    print("Hiding your treasure! X marks the spot.")
    position = input()  # Where do you want to put the treasure?
    # 🚨 Don't change the code above 👆
    # Write your code below this row 👇
    letter = position[0]
    number = int(position[1])

    letter_index = list('ABCDEFGHI')
    my_index = letter_index.index(letter)

    map[number-1][my_index] = 'X'
    print(map)

    # Write your code above this row 👆
    # 🚨 Don't change the code below 👇
    print(f"{line1}\n{line2}\n{line3}")


if __name__ == '__main__':
    start_app("Hello World")
