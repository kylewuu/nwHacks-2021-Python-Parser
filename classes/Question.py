class Question:
    def __init__(self, question_type, question, correct_answer, all_possible_answers=[]):
        self.question_type = question_type  # true_false, short_answer, mc
        self.question = question  # question in string format
        self.correct_answer = correct_answer  # correct answer in string format
        # all answers in an array of strings (only applies to multiple choice)
        self.all_possible_answers = all_possible_answers
