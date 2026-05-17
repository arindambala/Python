# Day 17 - 100 Days of Code

from Model import Question
from Data import question_set
from Func import Task

print(f"\n---- Quiz ^ Master ----\n")

question_bank = []
for question in question_set:
    question_text = question['Text']
    question_answer = question['Answer']
    
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# print(question_bank)
quiz = Task(question_bank)

while quiz.more_questions():
    quiz.question_cycle()

print("\n\n ---- Congratulations! ---- \n")
print(f"|> FINAL SCORE : {quiz.score}/{len(question_bank)}")