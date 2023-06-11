import time
import sys

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer.lower() == self.answer.lower()

class QuizGame:
    def __init__(self):
        self.questions = []
        self.load_questions()

    def load_questions(self):
        # Add your questions and answers here
        q1 = Question("Question 1 ...", "")
        q2 = Question("Question 2 ...", "")
        q3 = Question("Question 3 ...", "")

        self.questions.extend([q1, q2, q3])

    def play(self):
        print("Welcome to CodeVer Quiz Game!")
        player_name = input("Enter Your Name: ")
        time.sleep(2)
        player_age = int(input("Enter Your Age: "))
        time.sleep(2)
        player_gender = input("Enter Your Preferred Gender: ")
        time.sleep(2)

        if player_age <= 17 and player_gender == "":
            print("Requirement Not Met!")
            sys.exit()

        print("\nGame Instructions:")
        print("1. CodeVer is a Trivia Quiz Game. Every question is based on reality and tech.")
        print("2. To answer a question, simply type your answer.")
        print("3. To exit the game, type 'exit' at any time.")
        print("4. Good luck!\n")

        score = 0
        total_questions = len(self.questions)

        for i, question in enumerate(self.questions):
            print(f"Question {i+1} ...")
            time.sleep(2)
            user_answer = input("Your Answer: ")

            if user_answer.lower() == 'exit':
                sys.exit()

            if question.check_answer(user_answer):
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")

            print()

        print("Quiz Completed!")
        print(f"Player: {player_name}")
        print(f"Score: {score}/{total_questions}")

quiz_game = QuizGame()
quiz_game.play()
