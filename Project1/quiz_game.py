def quiz_game():
    print("Welcome to the Quiz Game!")
    print("Answer the following questions by typing the letter of your choice.\n")

    # List of questions, choices, and answers
    questions = [
        {
            "question": "What is the capital of France?",
            "choices": ["a) Paris", "b) London", "c) Rome", "d) Berlin"],
            "answer": "a"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "choices": ["a) Earth", "b) Venus", "c) Mars", "d) Jupiter"],
            "answer": "c"
        },
        {
            "question": "What is the largest mammal?",
            "choices": ["a) Elephant", "b) Blue Whale", "c) Giraffe", "d) Polar Bear"],
            "answer": "b"
        },
        {
            "question": "Who wrote 'Hamlet'?",
            "choices": ["a) Charles Dickens", "b) William Shakespeare", "c) Jane Austen", "d) Mark Twain"],
            "answer": "b"
        },
        {
            "question": "What is the boiling point of water in Celsius?",
            "choices": ["a) 90", "b) 80", "c) 100", "d) 120"],
            "answer": "c"
        },
    ]

    score = 0

    # Iterate through the questions
    for i, q in enumerate(questions, start=1):
        print(f"Question {i}: {q['question']}")
        for choice in q['choices']:
            print(choice)
        
        while True:
            answer = input("Your answer: ").strip().lower()
            if answer in ['a', 'b', 'c', 'd']:
                break
            else:
                print("Error: Please enter a valid option (a, b, c, or d).")

        if answer == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was '{q['answer']}'.\n")

    # Final score
    print(f"Your final score is {score}/{len(questions)}")
    if score == len(questions):
        print("Excellent work! You got a perfect score!")
    elif score >= len(questions) // 2:
        print("Good job! You did well!")
    else:
        print("Better luck next time!")

if __name__ == "__main__":
    quiz_game()