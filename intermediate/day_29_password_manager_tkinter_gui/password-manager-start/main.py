from tkinter import *

def start_app():

    # ---------------------------- PASSWORD GENERATOR ------------------------------- #

    # ---------------------------- SAVE PASSWORD ------------------------------- #

    # ---------------------------- UI SETUP ------------------------------- #
    window = Tk()
    window.title("Password Manager")
    window.config(padx=20, pady=20)

    canvas = Canvas(width=300, height=300)
    logo_img = PhotoImage(file="logo.png")
    canvas.create_image(200, 189, image=logo_img)
    canvas.grid(row=0, column=1)  # To make an element using 2 columns - use 'columnspan'

    website_label = Label(text="Website:")
    website_label.grid(row=1, column=0)

    username_label = Label(text="Email / Username:")
    username_label.grid(row=2, column=0)

    password_label = Label(text="Password:")
    password_label.grid(row=3, column=0)

    website_input = Entry(width=35)
    website_input.grid(row=1, column=1, columnspan=2)

    email_input = Entry(width=35)
    email_input.grid(row=2, column=1, columnspan=2)

    password_input = Entry(width=21)
    password_input.grid(row=3, column=1)

    gen_passw_button = Button(text="Generate Password", width=14)
    gen_passw_button.grid(row=3, column=2)

    add_button = Button(text="Add", width=36)
    add_button.grid(row=4, column=1, columnspan=2)


    window.mainloop()


if __name__ == "__main__":
    start_app()
