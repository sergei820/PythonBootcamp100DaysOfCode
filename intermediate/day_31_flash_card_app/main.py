import time
from tkinter import *
import pandas
from random import randint

BACKGROUND_COLOR = "#B1DDC6"
card_back_path = "images/card_back.png"
card_front_path = "images/card_front.png"
right_answer_path = "images/right.png"
wrong_answer_path = "images/wrong.png"

english_words_file = "data/c1_english_words.csv"





def start_app():
    data = pandas.read_csv(english_words_file)
    dicts_list = data.to_dict(orient="records")

    studying_language = "English"
    base_language = "Russian"

    window = Tk()
    window.title("Flash Cards App")
    window.config(padx=50, pady=50, background=BACKGROUND_COLOR)
    card_front_image = PhotoImage(file=card_front_path)
    card_back_image = PhotoImage(file=card_back_path)

    canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, borderwidth=0)

    canvas_card_image = canvas.create_image(400, 263, image=card_front_image)  # args should point to the center of the canvas
    language_title = canvas.create_text(400, 150, text="", font=("Ariel", 35, "italic"))
    new_word = canvas.create_text(400, 250, text="", font=("Ariel", 40, "bold"))

    canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
    canvas.grid(row=0, column=0, columnspan=2)

    def next_card():
        index = randint(0, 50)
        words_pair = dicts_list[index]

        # ENGLISH SIDE
        canvas.itemconfig(canvas_card_image, image=card_front_image)
        canvas.itemconfig(language_title, text=studying_language)
        canvas.itemconfig(new_word, text=words_pair.get(studying_language))
        canvas.grid(row=0, column=0, columnspan=2)

        # TURNING THE CARD
        canvas.itemconfig(canvas_card_image, image=card_back_image)
        canvas.itemconfig(language_title, text="Translation")
        canvas.itemconfig(new_word, text=words_pair.get(base_language))
        canvas.grid(row=0, column=0, columnspan=2)


    wrong_answer_image = PhotoImage(file=wrong_answer_path)
    wrong_answer_button = Button(image=wrong_answer_image, highlightthickness=0, command=next_card)
    wrong_answer_button.grid(row=1, column=0)

    right_answer_image = PhotoImage(file=right_answer_path)
    right_answer_button = Button(image=right_answer_image, highlightthickness=0, command=next_card)
    right_answer_button.grid(row=1, column=1)

    next_card()


    window.mainloop()


if __name__ == "__main__":
    start_app()
