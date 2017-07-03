#'10 Questions'

questions = {"Which language are we learing now?" : "python", 
            "What veersion of python are we using?" : "3.6",
            "What type is this: 'abc'?" : "str",
            "What type is this: '56.988'?" : "float",
            "What function can count the lenght of expression?" : "len",
            "What will be in output 'True or False'?" : "True",
            "What will be in output 'True and False'?" : "False",
            "What will be in output '4 % 5'?" : "1",
            "What will be in output '2**3'?" : "8",
            "Do you like learning python?" : "yes"}
 
 
question_count = 0
correct_answers = 0

for question, answer in questions.items():
    question_count += 1
    user_answer = input(question + "\n")
    user_answer = user_answer.lower()
    if user_answer == answer.lower():
        print("That's correct")
        correct_answers += 1
    else:
        print("You're wrong!")

print("Total answers: ", question_count, "Total correct answers: ", correct_answers)
