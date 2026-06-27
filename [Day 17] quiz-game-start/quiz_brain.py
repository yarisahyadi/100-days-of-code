class QuizBrain:
    def _init_(self, question_list):
        self.question_number = 0
        self.question_list = question_list

    def still_has_question(self):
        return self.question_number != len(self.question_list)

    def next_question(self):
        self.current_question = self.question_list[self.question_number].text
        self.question_number += 1
        input(f"Q.{self.question_number} {self.current_question} (True/False)?: ")
