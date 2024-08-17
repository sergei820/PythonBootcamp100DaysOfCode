def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1*n2


def divide(n1, n2):
    return n1/n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}


def calculate(a=None):
    if a is None:
        a = int(input("Choose first number: "))
    operator = input("Choose the operation: ")
    b = int(input("Choose second number: "))

    if operator in operations:
        result = operations[operator](a, b)
        print(f"Result is: {result}")
        proceed = input("If you want to continue from the result, type 'y', else type 'n'\n")
        if proceed == 'y':
            calculate(result)
        elif proceed == 'n':
            calculate()


if __name__ == "__main__":
    calculate()
