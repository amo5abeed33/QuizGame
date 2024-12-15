import tkinter as tk
from tkinter import messagebox


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")

        self.questions = [
            ("What is the full form of CPU?", "Central Processing Unit"),
            ("Which gate gives low in both HIGH input?", "NAND"),
            ("What does HTML stand for?", "HyperText Markup Language"),
            ("What is the capital of USA?", "Washington DC"),
            ("Who is known as the father of the computer?", "Charles Babbage")
        ]

        self.score = 0
        self.question_index = 0
        self.total_questions = len(self.questions)

        self.question_label = tk.Label(self.root, text=self.questions[self.question_index][0], font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.answer_entry = tk.Entry(self.root, font=("Arial", 14))
        self.answer_entry.pack(pady=10)

        self.submit_button = tk.Button(self.root, text="Submit Answer", command=self.check_answer, font=("Arial", 14))
        self.submit_button.pack(pady=10)

        self.result_label = tk.Label(self.root, text="", font=("Arial", 14))
        self.result_label.pack(pady=20)

    def check_answer(self):
        user_answer = self.answer_entry.get().strip().lower()
        correct_answer = self.questions[self.question_index][1].lower()

        if user_answer == correct_answer:
            self.score += 5
        else:
            self.score -= 2

        self.question_index += 1
        self.answer_entry.delete(0, tk.END)

        if self.question_index < self.total_questions:
            self.question_label.config(text=self.questions[self.question_index][0])
        else:
            self.show_result()

    def show_result(self):
        pass_mark = self.total_questions * 5 * 0.6  # 60% of max score

        if self.score >= pass_mark:
            result_text = f"Your total score is: {self.score}\nYou passed the quiz!"
        else:
            result_text = f"Your total score is: {self.score}\nYou failed the quiz. Better luck next time!"

        messagebox.showinfo("Quiz Finished", result_text)

        play_again = messagebox.askyesno("Play Again?", "Do you want to play again?")
        if play_again:
            self.reset_quiz()
        else:
            self.root.quit()

    def reset_quiz(self):
        self.score = 0
        self.question_index = 0
        self.question_label.config(text=self.questions[self.question_index][0])
        self.result_label.config(text="")
        self.answer_entry.delete(0, tk.END)


root = tk.Tk()

quiz_app = QuizApp(root)

root.mainloop()
