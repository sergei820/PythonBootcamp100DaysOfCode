from tkinter import *

def start_app():
    window = Tk()
    window.title("GUI title")
    window.minsize(width=500, height=300)

    # Label
    my_label = Label(text="New Label", font=("Arial", 16, "bold"))
    my_label.pack(side="left")

    # Entry (Input)
    input_text = Entry(width=15)
    input_text.pack()

    def button_clicked():
        user_input = input_text.get()
        my_label.config(text=user_input)
        my_label.pack(side="left")

    # Button
    button = Button(text="Click me", command=button_clicked)
    button.pack()




    window.mainloop()


if __name__ == "__main__":
    start_app()
