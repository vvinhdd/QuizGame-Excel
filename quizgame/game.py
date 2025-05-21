import random

class QuizGame:
    def __init__(self, df):
        self.df = df
        self.list_group = df['Group'].unique()
        self.random_choice = random.choice(self.list_group)
        self.question_choice = df[df['Group'] == self.random_choice].reset_index(drop=True)
        self.answers_choice = self.question_choice['Answer'].tolist()
        self.selected_columns = ['Answer', 'W1', 'W2', 'W3']
        self.user_answers = {}
        self.current_index = 0
        self.list_choice_done = self.shuffle_choices()

    def shuffle_choices(self):
        re_choice = []
        for i in range(len(self.question_choice)):
            row_values = self.question_choice.iloc[i][self.selected_columns]
            list_choices = row_values.tolist()
            random.shuffle(list_choices)
            re_choice.append(list_choices)
        return re_choice

    def get_question(self, index):
        return self.question_choice["Question"].iloc[index]

    def get_choices(self, index):
        return self.list_choice_done[index]

    def save_answer(self, index, answer):
        self.user_answers[index] = answer

    def check_answer(self, index):
        if index in self.user_answers:
            return self.user_answers[index] == self.answers_choice[index]
        return False

    def get_score(self):
        score = 0
        for i in range(len(self.question_choice)):
            if self.check_answer(i):
                score += 1
        return score

    def total_questions(self):
        return len(self.question_choice)
