name = ""
contact = ""
enrollno = ""
username = ""
quiz_choice = ""

questions = {
    "python": [
        {
            'question': 'What is Python?',
            'options': ['A type of snake', 'A programming language', 'A bird', 'A dessert'],
            'correct_answer': 'A programming language',
        },
        {
            'question': 'Which of the following is true about Python?',
            'options': ['It is statically typed', 'It is dynamically typed', 'It is compiled', 'It is platform-dependent'],
            'correct_answer': 'It is dynamically typed',
        },
    ],
    "java": [
        {
            'question': 'What is Java?',
            'options': ['A programming language', 'A type of coffee', 'An island', 'A fruit'],
            'correct_answer': 'A programming language',
        },
        {
            'question': 'What is the main purpose of Java?',
            'options': ['Web development', 'Game development', 'Mobile app development', 'Platform-independent programming'],
            'correct_answer': 'Platform-independent programming',
        },
    ],
    "c": [
        {
            'question': 'What is C?',
            'options': ['A programming language', 'A vitamin', 'A type of car', 'A musical note'],
            'correct_answer': 'A programming language',
        },
        {
            'question': 'C is known for its:',
            'options': ['Simplicity', 'Complexity', 'Colorful syntax', 'Object-oriented features'],
            'correct_answer': 'Simplicity',
        },
    ],
    "c++": [
        {
            'question' : 'Who invented C++?',
            'options' :  ['Dennis Ritchie','Ken Thompson','Brian Kernighan','Bjarne Stroustrup'],
            'correct_answer' : 'Bjarne Stroustrup'
        },
        {
            'question' : 'Which of the following user-defined header file extension used in c++?',
            'options' : ['hg','cpp','py','c'],
            'correct_answer' : 'cpp'
        }
    ]
}

def welcome_message():
    global name, contact, email, quiz_choice
    print("Welcome to the Quiz Application!")
    print("Please fill in your details:")
    name = input("Name: ")
    contact = input("Contact: ")
    enrollno = input("Enrollnment: ")
    username = input("Username: ")
    print("Choose a quiz:")
    print("1. Python")
    print("2. Java")
    print("3. C")
    print("4. C++")
    quiz_choice = input("Enter the number of your choice (1/2/3/4): ")
    return quiz_choice

def start_quiz(selected_quiz):
    global name
    quiz = selected_quiz.lower()
    score = 0
    if quiz in questions:
        quiz_questions = questions[quiz]
        for q in quiz_questions:
            print(q['question'])
            for i, option in enumerate(q['options'], 1):
                print(f"{i}. {option}")
            user_answer = input("Your answer (enter the option number): ")
            try:
                user_answer = int(user_answer)
                if 1 <= user_answer <= len(q['options']):
                    if q['options'][user_answer - 1] == q['correct_answer']:
                        score += 1
                else:
                    print("Invalid option number. Please choose a valid option.")
            except ValueError:
                print("Invalid input. Please enter the option number.")
        print(f"Hello {name}, your {quiz} marks is {score}/{len(quiz_questions)}")

while True:
    quiz_choice = welcome_message()
    if quiz_choice == "1":
        start_quiz("python")
    elif quiz_choice == "2":
        start_quiz("java")
    elif quiz_choice == "3":
        start_quiz("c")
    elif quiz_choice == "4":
        start_quiz("c++")
    else:
        print("Invalid choice. Please select a valid quiz.")
        continue

    choice = input("Do you want to logout? (yes/no): ")
    if choice.lower() == "yes":
        break
