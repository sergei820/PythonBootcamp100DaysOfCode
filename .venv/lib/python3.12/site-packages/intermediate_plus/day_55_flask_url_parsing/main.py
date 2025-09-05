from flask import Flask
app = Flask(__name__)


def bold_decorator(function):
    def wrapper():
        return f"<b>{function()}</b>"
    return wrapper

def em_decorator(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def underlined_decorator(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper

@app.route('/')
def render_index():
    return '<br/>' \
    '<h2 style="text-align: center">Hello, welcome!</h2>' \
    '<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMHFiZDF4bDE4a25reGg1M2ptcjNrY3pzMm8waTF1dzhpd2ZmenNncyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/QvBoMEcQ7DQXK/giphy.gif">'

@app.route('/bye')
@bold_decorator
@em_decorator
@underlined_decorator
def bye():
    return "Bye!"

@app.route('/<username>')
def greet(username):
    return f"Hello, {username}!"


if __name__ == "__main__":
    app.run(debug=True)
