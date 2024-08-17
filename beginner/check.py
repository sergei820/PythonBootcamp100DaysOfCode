import random
import math


def start_app():
    def mutate(a_list):
        b_list = []
        new_item = 0
        for item in a_list:
            new_item = item * 2
            new_item += random.randint(1, 3)
            new_item = math.add(new_item, item)


if __name__ == '__main__':
    start_app()
