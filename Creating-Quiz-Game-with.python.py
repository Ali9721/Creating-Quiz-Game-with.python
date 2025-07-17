# At first, Import "random" library & define "QUIZ_FILE" as a variable.
import random

QUIZ_FILE = 'quiz.txt'

# Load quiz questions.
def load_quiz(filename):
    try:
        with open(filename,"r") as file:
            lines = file.readlines()
            return [line.strip().split("|") for line in lines if line.strip()]
    except FileNotFoundError:
        print("Quiz file not found! please ensure the file exists.")
        return []

# run quiz questions.

def run_quiz(questions):
    random.shuffle(questions)
    score = 0
    for question, *options, correct in questions:
        print(f"\n{question}")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        while True:
            try:
                answer = int(input("Your answer (enter the option number): "))
                if 1 <= answer <= len(options):
                    break
                else:
                    print(f"Please choose a number between 1 and {len(options)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

        if options[answer - 1 ] == correct:
            print("correct!")
            score += 1
        else:
            print(f"Wrong! The Correct answer was: {correct}")
    print(f"\n You scored{score}/{len(questions)}")

# Main program.
def main(): 
    print("Welcome to the quiz game!")
    questions = load_quiz(QUIZ_FILE)
    if not questions:
        return
    
    while True:
        run_quiz(questions)
        replay = input("\nDo you want to retake the quiz? (yes/no)").strip().lower()
        if replay not in ("yes",'y'):
            print("Thank you for playing! goodbye!")
            break

# Run main dictionary
if __name__ == "__main__":
    main()