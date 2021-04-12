import sys
class QuizBrain:
    def __init__(self, questions):
        self.answer_options = {'True':["+", "yes", "true"], 'False':["-", "no", "false"]}
        self.questions = questions

    def start(self):
        try:
            correct_answers = 0
            print("Hello dear player! It's time to test you knowledge in computer field\n\
You'll be asked 10 questions where you have to answer yes/true/+ or no/false/-\n\
To exit game press Ctrl+C\n")
            i = 1
            for q in self.questions:
                print("Question {}: {}".format(i, q.question))
                i += 1
                answer = self.player_answer()
                if answer in self.answer_options[q.correct_answer]:
                    correct_answers += 1
                    print("Correct!")
                else:
                    print("Incorrect!")
            print("\nGame ended. Your results\nCorrect answers {}".format(correct_answers))
        except KeyboardInterrupt:
            print("\nGame stopped!")
            sys.exit()

    def player_answer(self):
        error = True
        while error:
            try:
                answer = input("Your answer: ").lower()
                if answer not in self.answer_options['True'] + self.answer_options['False']:
                    raise ValueError("Incorrect answer word. Please type yes/true/+ for True or no/false/- for False")
                return answer
            except ValueError as e:
                print(e)
            except Exception as e:
                print(e)
