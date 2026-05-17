class Task:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
    
    def more_questions(self):
        return self.question_number < len(self.question_list)
    
    def answer_check(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("\n\n|> Right answer! \n")
        else:
            print(f"\n\n|> INCORRECT! || Correct Answer : {correct_answer}\n")
        print(f"|> CURRENT SCORE : {self.score}/{self.question_number} \n\n")
    
    def question_cycle(self):
        curr_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}) {curr_question.text} - (True | False) ? : ")
        self.answer_check(user_answer, curr_question.answer)