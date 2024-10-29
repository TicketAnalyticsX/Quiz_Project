class QuizBrain:

    def __init__(self, q_list):

        self.question = 0
        self.question_list = q_list
        self.score = 0

    def still_has_question(self):

        return self.question < len(self.question_list)

    def next_question(self):

        current_question = self.question_list[self.question]
        self.question += 1
        user_answer = input(f"Q.{self.question}: {current_question.text} (True/False):")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):

        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong!")
        print(f"The correct answer is {correct_answer}.")
        print(f"Your score is {self.score}/{self.question}.")





