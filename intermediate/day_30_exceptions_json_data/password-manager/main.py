from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json


def start_app():
    file_name = 'passwords.json'
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
        new_data = {
            website: {
                "email": email,
                "password": password,
            }
        }

        if len(website) == 0 or len(email) == 0 or len(password) == 0:
            messagebox.showerror(title="Oops!", message="Please, fill in all the fields!")
        else:
            is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email}\n"
                                                      f"Password: {password}\nWould you like to save the data?")

            if is_ok:
                pyperclip.copy(password)
                print("password copied to clipboard")
                try:
                    with open(file_name, "r") as data_file:
                        data = json.load(data_file)  # Reading old data
                        # data.update(new_data)  # Updating old data
                except FileNotFoundError:
                    # with open(file_name, "w") as data_file:
                    #     json.dump(new_data, data_file, indent=4)
                    data = {}
                data.update(new_data)  # Updating old data
                with open(file_name, "w") as data_file:
                    json.dump(data, data_file, indent=4)  # Saving the updated data

                website_input.delete(0, END)
                password_input.delete(0, END)
                # messagebox.showinfo("Your password is saved and copied to the clipboard!")
                website_input.focus()

    # ---------------------------- FIND PASSWORD ------------------------------- #
    def find_password():
        website = website_input.get()

        with open(file_name, "r") as data_file:
            data = json.load(data_file)
            try:
                email = data[website].get("email")
                password = data[website].get("password")
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            except FileNotFoundError:
                messagebox.showerror(title="Error", message="No data file found")
            except KeyError:
                messagebox.showerror(title="Error", message="No details for the website exists")

        # BEST OPTION
        try:
            with open(file_name, "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="No data file found")
        else:
            if website in data:  # it's better to use if/else then exceptions if possible
                email = data[website].get("email")
                password = data[website].get("password")
                messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
            else:
                messagebox.showerror(title="Error", message="No details for the website exists")

    # ---------------------------- UI SETUP ------------------------------- #
    window = Tk()
    window.title("Password Manager")
    window.config(padx=30, pady=30)

    canvas = Canvas(width=200, height=200)
    logo_img = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo_img)
    canvas.grid(row=0, column=1)  # To make an element using 2 columns - use 'columnspan'

    website_label = Label(text="Website:", width=21)
    website_label.grid(row=1, column=0)

    username_label = Label(text="Email / Username:")
    username_label.grid(row=2, column=0)

    password_label = Label(text="Password:")
    password_label.grid(row=3, column=0)

    website_input = Entry(width=21)
    website_input.grid(row=1, column=1)
    website_input.focus()

    search_button = Button(text="Search", width=14, command=find_password)
    search_button.grid(row=1, column=2)

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
