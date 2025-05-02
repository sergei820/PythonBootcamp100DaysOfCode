from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
card_back_path = "/images/card_back.png"
card_front_path = "images/card_front.png"
right_answer_path = "/images/card_back.png"
wrong_answer_path = "/images/card_back.png"


def start_app():
    window = Tk()
    window.title("Flash Cards App")
    window.config(padx=50, pady=50)

    canvas = Canvas(width=1000, height=700, background=BACKGROUND_COLOR)
    logo_img = PhotoImage(file=card_front_path)
    canvas.create_image(500, 326, image=logo_img)
    canvas.grid(row=0, column=0, columnspan=2)



    window.mainloop()


if __name__ == "__main__":
    start_app()
