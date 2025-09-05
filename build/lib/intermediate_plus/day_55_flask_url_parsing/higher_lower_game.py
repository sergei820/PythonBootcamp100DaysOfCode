from flask import Flask
app = Flask(__name__)
from random import randint

number_to_guess: int = randint(0, 10)

@app.route('/')
def start_index():
    return f'<h1>Guess a number between 0 and 9</h1>' \
            f'<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route('/<int:user_number>')
def check_number(user_number):
    if user_number > number_to_guess:
        return f'<h1 color="red">Too high, try again!</h1>' \
               f'<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    if user_number < number_to_guess:
        return f'<h1 color="red">Too low, try again!</h1>' \
               f'<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    else:
        return f'<h1 color="red">You found me!</h1>' \
               f'<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'



if __name__ == "__main__":
    print(number_to_guess)
    app.run(debug=True)
