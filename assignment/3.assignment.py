print("Welcome to the Python Quiz Challenge!")
quiz = {
    "Q1: What does 'int' stand for in Python?": {
        "choices": ["A. integer", "B. input", "C. interval", "D. instance"],
        "answer": "a"
    },
    "Q2: What is the output of 3 ** 2?": {
        "choices": ["A. 6", "B. 9", "C. 8", "D. 5"],
        "answer": "b"
    },
    "Q3: Which keyword is used to define a function in Python?": {
        "choices": ["A. def", "B. func", "C. lambda", "D. define"],
        "answer": "a"
    },
    "Q4: What does the '%' operator do in Python?": {
        "choices": ["A. Division", "B. Exponentiation", "C. Modulus (remainder)", "D. Floor Division"],
        "answer": "c"
    },
    "Q5: Which of these is a valid variable name?": {
        "choices": ["A. 2value", "B. my-var", "C. my_var", "D. class"],
        "answer": "c"
    },
    "Q6: What is the output of print(10 // 3)?": {
        "choices": ["A. 3", "B. 3.33", "C. 4", "D. 3.0"],
        "answer": "a"
    },
    "Q7: How do you start a comment in Python?": {
        "choices": ["A. //", "B. /*", "C. #", "D. <!--"],
        "answer": "c"
    },
    "Q8: What data type is the result of: input('Enter: ')?": {
        "choices": ["A. int", "B. str", "C. float", "D. bool"],
        "answer": "b"
    },
    "Q9: What does len('hello') return?": {
        "choices": ["A. 5", "B. 4", "C. 6", "D. Error"],
        "answer": "a"
    },
    "Q10: Which keyword is used to create a loop that runs a specific number of times?": {
        "choices": ["A. for", "B. while", "C. loop", "D. repeat"],
        "answer": "a"
    },
    "Q11: Which of these is a Python list?": {
        "choices": ["A. (1, 2, 3)", "B. {1, 2, 3}", "C. [1, 2, 3]", "D. <1, 2, 3>"],
        "answer": "c"
    },
    "Q12: What is used to handle exceptions in Python?": {
        "choices": ["A. try/except", "B. catch", "C. throw", "D. error"],
        "answer": "a"
    },
    "Q13: What is the correct file extension for a Python file?": {
        "choices": ["A. .py", "B. .python", "C. .pt", "D. .pyt"],
        "answer": "a"
    }
}

score = 0

for question, info in quiz.items():
    print("\n" + question)
    for choice in info["choices"]:
        print(choice)
    user_answer = input("Your answer (A/B/C/D): ").lower()
    
    if user_answer == info["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! Correct answer: {info['answer'].upper()}")

print(f"\n Your final score: {score}/{len(quiz)}")
if score == 13:
    print("You're a Python Master!")
elif score >= 10:
    print("Excellent work!")
elif score >= 7:
    print("You're getting good!")
elif score >= 4:
    print("Keep going, you're learning!")
else:
    print("Don't give up — keep practicing!")