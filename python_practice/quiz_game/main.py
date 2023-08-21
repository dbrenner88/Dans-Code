from question_model import *
from quiz_brain import *
from trivia_api import *
from html import *

question_bank = []
question_data = []
has_data = False

while not has_data:

    level_selection = user_level(pick_level())

    category_selection = user_category(select_category(fetch_categories()))

    question_data = fetch_questions(level_selection, category_selection)

    if "Code" in question_data:
        print(
            f"\nThere was an error.\n{question_data}\nPlease select again.\n")
    else:
        has_data = True


for entry in question_data:
    question_text = unescape(entry['question'])
    question_answer = entry['correct_answer']
    new_question = QuestionModel(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print(
    f"Congrats! You've completed the quiz!\nYour final score was: {quiz.score}/{quiz.question_number}\n")
