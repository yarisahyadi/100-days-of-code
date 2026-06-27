import data
import question_model
import quiz_brain

QUESTIONS_DATA = data.question_data
QuestionModel = question_model.Question
QuizBrain = quiz_brain.QuizBrain
questions = []

for data in QUESTIONS_DATA:
    question = QuestionModel(data["text"], data["answer"])
    questions.append(question)

while QuizBrain(questions).still_has_question():
    answer = QuizBrain(questions).next_question()
    QuizBrain(questions).question_number += 1
