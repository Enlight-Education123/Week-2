# --- Quiz Project ---

# TODO: Create 5 quiz questions with prompts and answers
questions = [
    {"prompt": "2+2\n", "answer": "4"},
    {"prompt": "4+6\n", "answer": "10"},
    {"prompt": "4*99\n", "answer": "396"},
    {"prompt": "2*900\n", "answer": "1800"},
    {"prompt": "56*54\n", "answer": "3024"}
    ]
    

    # Example format:
    # {"prompt": "What is 2 + 2?", "answer": "4"},
    # {"prompt": "Capital of France?", "answer": "Paris"}


# Initialize score
score = 0

# Loop through each question
for q in questions:
   
        user_input = input(q["prompt"] + "Your answer: ").strip().lower()

# Handle blank input
        if user_input == "":
            print("Please enter an answer.")
            continue

        if user_input == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect!")        
            
    

print(f"You got {score} out of {len(questions)} correct!")
