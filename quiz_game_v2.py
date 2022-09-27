import json
import random
import unittest
from unittest.mock import patch


class Quiz_Game:
    def __init__(self, filename):
        file = open(filename)
        self.questions = json.load(file)
        file.close()
        self.points = 0

    # def shuffle_answers(self, answers_list):
    #     random.shuffle(answers_list)
    #     return answers_list

    def shuffle_list(self, list):
        random.shuffle(list)
        return list

    def print_questions_and_answers(self):
        question_list = self.questions["questions"]
        self.shuffle_list(question_list)
        questions_number = len(self.questions["questions"])
        for number in range(0, questions_number):
            question_index = number
            question, shuffled_answers, good_answer = self.get_question_and_answer_by_index(question_index)
            print(question)
            for answer in shuffled_answers:
                print(answer)
            self.answer_and_earn_point(good_answer)

    def get_question_and_answer_by_index(self, question_index):
        question_list = self.questions["questions"]
        question_object = question_list[question_index]
        question = question_object["question"]
        answers = question_object["answers"]
        good_answer = answers[0]
        shuffled_answers = self.shuffle_list(answers)
        return question, shuffled_answers, good_answer

    def get_questions_and_answers(self):
        questions_number = len(self.questions["questions"])
        for number in range(0, questions_number):
            question_index = number
        return question_index

    def get_points(self):
        return self.points

    def answer_and_earn_point(self, good_answer):
        user_answer = self.answer_question()
        if user_answer == good_answer.lower():
            self.points = self.get_points() + 1
            print("Correct!")
        else:
            print("Wrong answer :(")


    def answer_question(self):
        user_answer = input("Your answer: ")
        return user_answer.lower()

    def get_input(self, text):
        return input(text)



# quiz1 = Quiz_Game("questions.json")
#print(quiz1.get_question_and_answer_by_index(0))
# print(quiz1.answer_and_earn_point())
# quiz1.print_questions_and_answers()






