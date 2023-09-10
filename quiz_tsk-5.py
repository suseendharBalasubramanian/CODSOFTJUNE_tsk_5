import random
import tkinter as tk
from tkinter import messagebox
import time

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")

        self.quiz_questions = [
            {
                "question": "What is the capital of France?",
                "choices": ["London", "Madrid", "Paris", "Rome"],
                "correct_answer": "Paris"
            },
            {
                "question": "Which planet is known as the Red Planet?",
                "choices": ["Mars", "Venus", "Earth", "Jupiter"],
                "correct_answer": "Mars"
            },
            {
                "question": "Which language has the most native speakers?",
                "choices": ["English", "Spanish", "Hindi", "Arabic"],
                "correct_answer": "Spanish"
            },
            {
                "question": "Aureolin is a shade of what color?",
                "choices": ["White", "Green", "Red", "Yellow"],
                "correct_answer": "Yellow"
            },
            {
                "question": "What year was the United Nations established?",
                "choices": ["1970", "1990", "1926", "1945"],
                "correct_answer": "1945"
            },
            {
                "question": "What is 5 multiplied by 9?",
                "choices": ["42", "45", "50", "55"],
                "correct_answer": "45"
            }
        ]

        self.score = 0
        self.current_question_index = 0
        self.timer_seconds = 10  # Set the timer duration in seconds

        self.question_label = tk.Label(root, text="", font=("Arial", 14))
        self.question_label.pack(pady=20)

        self.timer_label = tk.Label(root, text="", font=("Arial", 12))
        self.timer_label.pack()

        self.choice_buttons = []
        for i in range(4):
            button = tk.Button(root, text="", font=("Arial", 12), command=lambda i=i: self.check_answer(i))
            button.pack(fill="both", padx=20, pady=5)
            self.choice_buttons.append(button)

        self.finish_button = tk.Button(root, text="Finish", font=("Arial", 12), command=self.show_score)
        self.finish_button.pack(pady=20)

        self.next_button = tk.Button(root, text="Next", font=("Arial", 12), command=self.next_question, state="disabled")
        self.next_button.pack(pady=20)

        self.load_question()

    def load_question(self):
        if self.current_question_index < len(self.quiz_questions):
            question_data = self.quiz_questions[self.current_question_index]
            self.question_label.config(text=question_data["question"])
            choices = question_data["choices"]
            random.shuffle(choices)
            for i in range(4):
                self.choice_buttons[i].config(text=choices[i])
            self.next_button.config(state="disabled")
            self.start_timer()
        else:
            self.show_score()

    def start_timer(self):
        self.timer_value = self.timer_seconds
        self.update_timer()

    def update_timer(self):
        self.timer_label.config(text=f"Time left: {self.timer_value} seconds")
        if self.timer_value > 0:
            self.timer_value -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="Time's up!")
            self.check_answer(-1)  # -1 represents no answer selected

    def check_answer(self, choice_index):
        question_data = self.quiz_questions[self.current_question_index]
        correct_answer = question_data["correct_answer"]
        if choice_index == -1:
            user_answer = "Time's up!"
        else:
            user_answer = self.choice_buttons[choice_index].cget("text")
        if user_answer == correct_answer:
            self.score += 1
        self.current_question_index += 1
        self.next_button.config(state="active")
        for button in self.choice_buttons:
            button.config(state="disabled")

    def next_question(self):
        for button in self.choice_buttons:
            button.config(state="active")
        self.load_question()

    def show_score(self):
        messagebox.showinfo("Quiz Completed", f"Your Score: {self.score}/{len(self.quiz_questions)}")
        self.root.quit()

def main():
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
