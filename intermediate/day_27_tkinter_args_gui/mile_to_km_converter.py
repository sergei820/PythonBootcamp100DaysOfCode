from tkinter import *

def miles_to_km(miles: str):
    km = float(miles) * 1.609344
    return round(km, 3)


def start_app():
    window = Tk()
    window.title("Mile to Km Converter")
    window.minsize(width=500, height=300)
    window.config(padx=30, pady=30)

    # Entry (Input)
    input_text = Entry(width=15)
    input_text.grid(column=1, row=0)

    # Label "Miles"
    label_miles = Label(text="Miles", font=("Arial", 16, "bold"))
    label_miles.grid(column=2, row=0)

    # Label "is equal to"
    label_miles = Label(text="is equal to", font=("Arial", 16, "bold"))
    label_miles.grid(column=0, row=1)

    # Label "Km"
    label_kilometers = Label(text="Km", font=("Arial", 16, "bold"))
    label_kilometers.grid(column=2, row=1)

    def button_clicked():
        user_input = input_text.get()
        label_converted.config(text=miles_to_km(user_input))

    # Button "Calculate"
    button = Button(text="Calculate", command=button_clicked)
    button.grid(column=1, row=2)

    # Label "RESULT in Km" (* 1.609344)
    label_converted = Label(text="", font=("Arial", 16, "bold"))
    label_converted.grid(column=1, row=1)

    window.mainloop()


if __name__ == "__main__":
    start_app()
