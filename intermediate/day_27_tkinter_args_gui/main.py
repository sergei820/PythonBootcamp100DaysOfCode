import tkinter

def start_app():
    window = tkinter.Tk()
    window.title("GUI title")
    window.minsize(width=500, height=300)

    # Label
    my_label = tkinter.Label(text="New Label", font=("Arial", 16, "bold"))
    my_label.pack(side="left")


    window.mainloop()


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
    # start_app()
    # print(add(3, 5, 7))
    # calculate(2, add=3, multiply=5)
    car = Car(make="Mazda", model="2")
    print(car.model)
