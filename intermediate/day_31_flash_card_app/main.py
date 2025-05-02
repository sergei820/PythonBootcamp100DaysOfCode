from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
card_back_path = "images/card_back.png"
card_front_path = "images/card_front.png"
right_answer_path = "images/right.png"
wrong_answer_path = "images/wrong.png"


def start_app():
    window = Tk()
    window.title("Flash Cards App")
    window.config(padx=50, pady=50)

    canvas = Canvas(width=900, height=800, background=BACKGROUND_COLOR)
    logo_img = PhotoImage(file=card_front_path)
    canvas.create_image(500, 326, image=logo_img)
    canvas.grid(row=0, column=0, columnspan=2, rowspan=2)

    language_label = Label(text="English", bg="white", font=("Arial", 30, "italic"))
    language_label.grid(row=0, column=0, columnspan=2)

    foreign_word_label = Label(text="Word", bg="white", font=("Arial", 30, "bold"))
    foreign_word_label.grid(row=0, column=0, columnspan=2, rowspan=2)

    wrong_answer_button = Button(text="images/wrong.png")
    wrong_answer_button.grid(row=2, column=0)

    right_answer_button = Button(text="images/right.png")
    right_answer_button.grid(row=2, column=1)



    window.mainloop()


if __name__ == "__main__":
    start_app()
