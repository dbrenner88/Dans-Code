from html import *


class QuestionModel():
    def __init__(self, question_text, answer):
        self.question_text = question_text
        self.answer = answer

    def __str__(self):
        return f"This is your question: {self.question_text}\nThis is your answer: {self.answer}."


class Category():
    def __init__(self, id, cat_name):
        self.id = id
        self.cat_name = cat_name
