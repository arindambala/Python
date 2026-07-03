# Day 34 - 100 Days of Code

from Data import Info
from Func import Task
from Model import Template
from UI import Interface

print(f'\n---- Trivia ^ App ----\n')

ques_bank = []
for ques in Info:
    ques_text = ques['question']
    ques_answer = ques['correct_answer']
    
    new_ques = Template(ques_text, ques_answer)
    ques_bank.append(new_ques)

quiz = Task(ques_bank)
quizUI = Interface()

# while quiz.still_has_questions():
#     quiz.next_question()

print('Quiz Completed!')
print(f'Final Score : {quiz.score}/{quiz.question_number}')