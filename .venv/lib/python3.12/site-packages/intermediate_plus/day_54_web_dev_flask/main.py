import time

import requests
from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "Hello, World!"


def start_app():
#     requests.get("https://www.google.com")
    def outer_func():
        print("Outer")

        def nested_func():
            print("Nested")

        return nested_func

    inner_func = outer_func()
    inner_func()


def decorator_func_try():

    def delay_decorator(function):
        def wrapper_function():
            time.sleep(2)
            function()
            function()
        return wrapper_function

    @delay_decorator
    def say_hello():
        print("Hello")

    def say_bye():
        print("Bye")

    @delay_decorator
    def say_greeting():
        print("How are you?")

    say_hello()
    say_bye()
    say_greeting()




if __name__ == "__main__":
    # start_app()
    # app.run()
    decorator_func_try()
