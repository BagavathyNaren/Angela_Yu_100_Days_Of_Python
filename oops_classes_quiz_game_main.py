from oops_classes_quiz_game_data import question_data
from oops_classes_quiz_game_question_model import Question
from oops_classes_quiz_game_quiz_brain import QuizBrain

question_bank = []

for question in range(0,len(question_data["results"])-1):
    question_text = question_data["results"][question]["question"]
    question_answer = question_data["results"][question]["correct_answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
questions_left = quiz.still_has_questions
while questions_left:
    try:
         quiz.next_question()
    except IndexError:
         questions_left = False

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")