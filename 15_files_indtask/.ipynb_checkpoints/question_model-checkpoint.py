class Question:
    def __init__(self, json_question):
        self.question = json_question['question']
        self.correct_answer = json_question['correct_answer']

    def __str__(self):
        return f"Question: {self.question}"