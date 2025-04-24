
def fibonacci(n):
    result = []
    a, b = 0, 1
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result


def start_app():
    pass


if __name__ == "__main__":
    start_app()
    print(fibonacci(10))
