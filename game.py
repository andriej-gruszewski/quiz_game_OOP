from quiz_game_v2 import Quiz_Game

# Start Game
start_quiz = Quiz_Game("questions2.json")
name = input("What is your name?:  ")
print(f"Hey {name} ! Welcome in Quiz Game! For every correct answer, you get 1 point. Let's start the game!")
start_quiz.print_questions_and_answers()
print(f"Thank you for participating in game {name} !")
points = start_quiz.get_points()
print(f"Your score is {points} point(s)!")
