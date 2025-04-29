from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
check_signs = ""
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global check_signs
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer")
    check_sign.config(text="")
    check_signs = ""
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    global check_signs
    work_sec = 8 # WORK_MIN * 60
    short_break_sec = 5 # SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps in (0, 2, 4, 6):
        timer_label.config(text="Work", fg=RED)
        count_down(work_sec)
    elif reps in (1, 3, 5):
        check_signs += "✔"
        check_sign.config(text=check_signs)

        timer_label.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)
    elif reps == 7:
        timer_label.config(text="Good job! Let's rest now!", fg=GREEN)
        count_down(long_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global reps
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = "0" + str(count_sec)
    if count == 0:
        reps += 1
        start_timer()


    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    print(count)
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


timer_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_button.grid(row=2, column=2)

check_sign = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))  # "✔"
check_sign.grid(row=3, column=1)


window.mainloop()


