from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

button_true_path = "images/true.png"
button_false_path = "images/false.png"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=380, height=350, background="white", borderwidth=0)
        self.question_text = self.canvas.create_text(
            150, 125,
            width=230,
            text="Some text",
            font=("Arial", 18, "italic"),
            fill=THEME_COLOR
        )  # 150, 125 - use middle of the Canvas
        self.canvas.create_text(300, 250, text="", font=("Arial", 18, "italic"))
        self.canvas.grid(row=1, column=0, columnspan=2, pady=30)

        self.answer_true_image = PhotoImage(file=button_true_path)
        self.button_true = Button(image=self.answer_true_image, highlightthickness=0, background=THEME_COLOR, pady=20, command=self.press_true)
        self.button_true.grid(row=2, column=0)

        self.answer_false_image = PhotoImage(file=button_false_path)
        self.button_false = Button(image=self.answer_false_image, highlightthickness=0, background=THEME_COLOR, pady=20, command=self.press_false)
        self.button_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def press_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def press_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)





