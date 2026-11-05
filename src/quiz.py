
def quiz():
    print("\n--- Team Toolkit Quiz ---")

    questions = [
        {
            "question": "Which language are we using for this project?",
            "options": ["Java", "Python", "C++", "JavaScript"],
            "answer": 2
        },
        {
            "question": "What does CPU stand for?",
            "options": [
                "Central Processing Unit",
                "Computer Personal Unit",
                "Central Program Utility",
                "Control Processing User"
            ],
            "answer": 1
        },
        {
            "question": "Which data type stores True or False?",
            "options": ["String", "Integer", "Boolean", "Float"],
            "answer": 3
        }
    ]

    score = 0

    for i, q in enumerate(questions, start=1):
        print(f"\nQuestion {i}: {q['question']}")

        for number, option in enumerate(q["options"], start=1):
            print(f"{number}. {option}")

        try:
            choice = int(input("Enter your answer (1-4): "))

            if choice < 1 or choice > 4:
                print("Invalid choice!")
                continue

            if choice == q["answer"]:
                print("Correct!")
                score += 1
            else:
                print("Incorrect!")

        except ValueError:
            print("Please enter a valid number.")

    print("\nQuiz completed!")
    print("Your score:", score, "out of", len(questions))


if __name__ == "__main__":
    quiz()
