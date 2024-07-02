from questions_data import question_data

class QuizBrain:
    def __init__(self,question_list):
        self.question_number = 0
        self.question_list = question_list
    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number +=1
        input(f"Q. {self.question_number}: {current_question.text} (True/false)")
        
        
class Question:
    def __init__(self,text, answer):
        self.text =text
        self.answer = answer
    

question_bank = []
for i in question_data:
    question_text = i["text"]
    question_answer = i["answer"]
    new_question = Question(text=question_text,answer=question_answer)
    question_bank.append(new_question)
quizz = QuizBrain(question_bank)

quizz.next_question()
