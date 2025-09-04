from quizzler_app_question_model import Question
from quizzler_app_data import question_data
from quizzler_app_quiz_brain import QuizBrain
from quizzler_app_ui import QuizInterface


question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)