
def add(*args):
    result = 0
    for i in args:
        result += i
    return result


def calculate(n, **kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(key)
        print(value)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]


if __name__ == "__main__":
    print(add(3, 5, 7))
    calculate(2, add=3, multiply=5)
    car = Car(make="Mazda", model="2")
    print(car.model)
