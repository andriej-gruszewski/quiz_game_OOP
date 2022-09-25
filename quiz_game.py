import json
import random

class Quiz_Game:
    def __init__(self, filename):
        file = open(filename)
        self.questions = json.load(file)
        file.close()
        self.points = 0


    def shuffle_answers(self, answers_list):
        random.shuffle(answers_list)
        return answers_list


    def print_questions_and_answers(self):
        question_list = self.questions["questions"]
        for question_object in question_list:
            print(question_object["question"])
            answers = question_object["answers"]
            shuffled_answers = self.shuffle_answers(answers)
            for answer in shuffled_answers:
                print(answer)

    def get_question_and_answer_by_index(self, question_index):
        question_list = self.questions["questions"]
        question_object = question_list[question_index]
        question = question_object["question"]
        answers = question_object["answers"]
        good_answer = answers[0]
        shuffled_answers = self.shuffle_answers(answers)
        return question, shuffled_answers, good_answer

    def get_questions_and_answers(self):
        questions_number = len(self.questions["questions"])
        for number in range(0, questions_number):
            print(self.get_question_and_answer_by_index(number))

    def get_points(self):
        return self.points

    def get_point(self, answer):
        question_index = int(self.questions["questions"])
        good_answer = self.get_question_and_answer_by_index(question_index)

        if answer == good_answer:
            self.get_points() + 1
            return self.get_points()








quiz1 = Quiz_Game("questions2.json")
print(quiz1.get_questions_and_answers())


