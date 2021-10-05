"""
3 points.

Write a program that generates a short test of the addition of two-digit numbers. The test contains five questions.
The child taking the test enters their name at the start of the test. The program stores the name of the child and
their score out of five. It resets the test at the end, ready for the next child who will see the same questions.

The names and scores are output before the next test starts.
"""

from random import randint


def generate_questions():
    questions = []

    for _ in range(5):
        questions.append((randint(0, 9), randint(0, 9)))

    return questions


def is_number(val):
    try:
        int(val)
        return True
    except ValueError:
        return False


def start_test(questions):
    name = input("Enter your name: ")

    current_score = 0
    q = 0

    for question in questions:
        q += 1

        print(f"Q{q} of {len(questions)}: What is {question[0]} + {question[1]}?")

        answer = "a"
        while not is_number(answer):
            answer = input("> ")

        if int(answer) == question[0] + question[1]:
            print("Correct!")
            current_score += 1
        else:
            print("Incorrect!")

    return {"name": name, "score": current_score}


questions = generate_questions()

while True:
    results = start_test(questions)

    print(f"{results['name']} scored {results['score']} out of {len(questions)}\n\n")
