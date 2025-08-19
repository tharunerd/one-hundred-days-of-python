from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface
from tkinter import Tk

# Create a list of Question objects
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# Initialize the quiz logic
quiz = QuizBrain(question_bank)

# Initialize the GUI and pass the quiz logic
# window = Tk()
quiz_ui = QuizInterface(quiz)
# window.mainloop()
print("You've completed the quiz") 
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
