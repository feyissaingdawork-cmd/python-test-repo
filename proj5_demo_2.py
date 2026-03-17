"""
5)	Create a basic quiz game that:
•	Contains a list of 5 to 10 questions stored in a dictionary (or list of dictionaries [{}, {}] ).
•	Ask the user each question and records their answers.
•	At the end, displays:
o	The user's score (e.g., 7/10)
o	Correct answers for any questions they got wrong """

#This project is a simple quiz game written in Python. 
# The purpose of the program is to ask users multiple questions, collect their answers, 
# check whether the answers are correct, and then calculate the final score.


def game_quiz():
    choice = [
        {
            "Question": "What is the capital city of United State?", 
            "options": ["london", "Paris", "DC", "paris"],
            "answer": "DC"
        },
    
        {
            "Question": "which planet know is as ringed planet?", 
            "options": ['Earth', 'Saturn', 'Jupiter', 'Mars'],
            "answer": "Saturn"
        },
        
        {
            "Question": "What is 5 + 8 in python", 
            "options": [13, "5+8", 58, 85], 
            "answer": 13
        },
    
        {
            "Question": "who created python?", 
            "options": ["Zack", "Gate", "Mask", "Rossum"],
            "answer": "Rossum"
        },

        {
            "Question": "how many countries are in Africa?", 
            "options": [54, 198, 50, 48], 
            "answer": 54 
        }
    ]
    score = 0
    for i in choice:
        print("\n *** wellcome to the game quiz *** ")
        print("\n" + i["Question"])
        print("option:", i["options"])

        user_answer = input("inter your answer")

        if user_answer == str(i["answer"]):
            print("correct !")
            score += 1
        else:
            print("wrong! The correct answer is:", i["answer"])
    print("\nyour final score is:", score, "out of", len(choice))

game_quiz()