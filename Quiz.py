# --- Quiz Project ---

# TODO: Create 5 quiz questions with prompts and answers
questions = [
    {"prompt": "What is the first color of the rainbow?\n", "answer": "red"},
    {"prompt": "What is 3+3?\n", "answer": "6"},
    {"prompt": "What is the capital of Tennessee?\n", "answer": "nashville"},
    {"prompt": "What is 5*4?\n", "answer": "20"}, 
    {"prompt": "What is the fastest animal on Earth?\n", "answer": "periguine falcon"}
]

score = 0

for q in questions:
    user_input = input(q["prompt"] + "Your answer: ").strip().lower()

    user = input(q["prompt"]+" ")
    while user.strip() == "":
        user = input("Please enter an answer").strip().lower()

    if(user_input == q["answer"]):
        score+=1
        print("Correct!")
    else: 
        print("Wrong")

print(f"You got {score} out of {len(questions)} correct!") 