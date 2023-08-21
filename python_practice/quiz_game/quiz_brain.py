class QuizBrain():
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        """Takes in a questions from the question list and returns an 
        input asking if the statement is true or false"""
        question = self.question_list[self.question_number]
        correct_answer = question.answer
        self.question_number += 1
        valid_answers = ["true", "false"]
        while True:
            user_answer = input(
                f"Q{self.question_number}: {question.question_text} (True/False): ").lower()
            if user_answer in valid_answers:
                break
            else:
                print("Invalid Entry. Please enter True or False.  ")
        self.check_answer(str(correct_answer), str(user_answer.title()))

    def still_has_questions(self):
        """validates if there are any more questions in the question bank or not."""
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, users_answer):
        """checks if the answer was right or wrong and prints out the results"""
        if answer == users_answer:
            self.score += 1
            print(
                f"You got it right!")
        else:
            print(
                f"That's Wrong.")
        print(
            f"The correct answer was: {answer}.\nYour current score is: {self.score}/{self.question_number}\n")
