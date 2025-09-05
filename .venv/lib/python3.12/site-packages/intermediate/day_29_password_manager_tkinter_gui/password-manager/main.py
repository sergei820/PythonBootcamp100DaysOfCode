from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip

def start_app():
    file_name = 'passwords.txt'
    # ---------------------------- PASSWORD GENERATOR ------------------------------- #
    def generate_password():
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                   'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                   'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        password_list = [choice(letters) for _ in range(randint(8, 10))]
        password_list.extend([choice(symbols) for _ in range(randint(2, 4))])
        password_list.extend([choice(numbers) for _ in range(randint(2, 4))])

        shuffle(password_list)
        password = "".join(password_list)

        print(f"Your password is: {password}")
        password_input.insert(0, password)
    # ---------------------------- SAVE PASSWORD ------------------------------- #
    def save_password():
        website = website_input.get()
        email = email_input.get()
        password = password_input.get()

        if len(website) == 0 or len(email) == 0 or len(password) == 0:
            messagebox.showerror(title="Oops!", message="Please, fill in all the fields!")
        else:
            is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\n"
                                                      f"Password: {password}\nWould you like to save the data?")

            if is_ok:
                pyperclip.copy(password)
                print("password copied to clipboard")
                with open(file_name, 'a') as file:
                    file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0, END)
                password_input.delete(0, END)
                messagebox.showinfo("Your password is saved and copied to the clipboard!")
                website_input.focus()

    # ---------------------------- UI SETUP ------------------------------- #
    window = Tk()
    window.title("Password Manager")
    window.config(padx=30, pady=30)

    canvas = Canvas(width=200, height=200)
    logo_img = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo_img)
    canvas.grid(row=0, column=1)  # To make an element using 2 columns - use 'columnspan'

    website_label = Label(text="Website:")
    website_label.grid(row=1, column=0)

    username_label = Label(text="Email / Username:")
    username_label.grid(row=2, column=0)

    password_label = Label(text="Password:")
    password_label.grid(row=3, column=0)

    website_input = Entry(width=40)
    website_input.grid(row=1, column=1, columnspan=2)
    website_input.focus()

    email_input = Entry(width=40)
    email_input.grid(row=2, column=1, columnspan=2)
    email_input.insert(0, "sergei@gmail.com")

    password_input = Entry(width=21)
    password_input.grid(row=3, column=1)

    gen_passw_button = Button(text="Generate Password", width=14, command=generate_password)
    gen_passw_button.grid(row=3, column=2)

    add_button = Button(text="Add", width=38, command=save_password)
    add_button.grid(row=4, column=1, columnspan=2)


    window.mainloop()


if __name__ == "__main__":
    start_app()
