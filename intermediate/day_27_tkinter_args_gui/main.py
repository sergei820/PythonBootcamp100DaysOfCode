from tkinter import *

def start_app():
    window = Tk()
    window.title("GUI title")
    window.minsize(width=500, height=300)
    window.config(padx=30, pady=30)

    # Label
    my_label = Label(text="New Label", font=("Arial", 16, "bold"))
    my_label.grid(column=0, row=0)

    # Entry (Input)
    input_text = Entry(width=15)
    input_text.grid(column=3, row=2)

    def button_clicked():
        user_input = input_text.get()
        my_label.config(text=user_input)

    # Button
    button = Button(text="Click me", command=button_clicked)
    button.grid(column=1, row=1)

    button_new = Button(text="New Button")
    button_new.grid(column=2, row=0)

    window.mainloop()


if __name__ == "__main__":
    start_app()
