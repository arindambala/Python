class Task:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
    
    def question_cycle(self):
        curr_question = self.question_list[self.question_number]
        input(f"Q.{self.question_number}) {curr_question.text} - (True | False) ? : ")