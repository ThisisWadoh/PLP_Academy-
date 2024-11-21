def quiz():
    print("\nWelcome to the Javi Quiz!")

    #Multiple choice questions

    questions = [
        {
            "question": "Who is the current deputy president of Kenya?",
            "options": ["A. Kindiki", "B. Riggy_G", "C. Baba", "D. Mudavadi"],
            "answer": "A"
        },

        {
            "question": "Who is the greatest footballer of all time?",
            "options": ["A. CR7", "B. Pele", "C. Messi", "D. Maradona"],
            "answer": "C"
        },

        {
            "question": "Which is NOT a Python data type?",
            "options": ["A. String", "B. List", "C. Tuples", "D. Array"],
            "answer": "D"
        },

        {
            "question": "Which country won the 2022 World Cup?",
            "options": ["A. France", "B. Argentina", "C. Netherlands", "D. England"],
            "answer": "B"
        }

    ]

    score = 0

    #Loops through questions
    for i, q in enumerate(questions): 
        print(f"\nQuestion{i+1}: {q['question']}")
        for option in q["options"]:
            print(option)

        user_answer = input("\nYour answer (A/B/C/D): ") .strip().upper()   
        if user_answer == q["answer"]:
            print("Correct")
            score += 1
        else:
            print("Wrong")

    #Quiz complete
    print("\nQuiz complete!")

    print(f"\nYour score: {score}/{len(questions)} ")

    #Play again option
    play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
    if play_again == "yes":
        quiz()
    else:
        print("Thank you for playing, Goodbye!")

quiz()

