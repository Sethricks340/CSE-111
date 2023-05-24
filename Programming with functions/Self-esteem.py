
print()
print("This program is an implementation of the Rosenberg Self-Esteem Scale. \n\
This program will show you ten statements that you could possibly apply to yourself. \n\
Please rate how much you agree with each of the statements by responding with one of these four letters:")

print()
print("D means you strongly disagree with the statement.\n\
d means you disagree with the statement.\n\
a means you agree with the statement.\n\
A means you strongly agree with the statement.")
print()

def main():
    total_points = 0

    questions = ["1. I feel that I am a person of worth, at least on an equal plane with others.",
                "2. I feel that I have a number of good qualities.",
                "3. All in all, I am inclined to feel that I am a failure.",
                "4. I am able to do things as well as most other people.",
                "5. I feel I do not have much to be proud of.",
                "6. I take a positive attitude toward myself.",
                "7. On the whole, I am satisfied with myself.",
                "8. I wish I could have more respect for myself.",
                "9. I certainly feel useless at times.",
                "10. At times I think I am no good at all."]
    
    for i in range(0,10):
        print(questions[i])
        answer = input("Enter D, d, a, or A: ")

        total_points += compute_answer(i, answer)

    print(f"Your score is {total_points}")

def compute_answer(question_number, answer):
    "Computes the points for an answer to a question."

    if (question_number + 1) in(1, 2, 4, 6, 7):
        if answer == "D":
            points = 0
        elif answer == "d":
                points = 1
        elif answer == "a":
                points = 2
        elif answer == "A":
                points = 3

    elif (question_number + 1) in(3, 5, 8, 9, 10):
        if answer == "D":
            points = 3
        elif answer == "d":
                points = 2
        elif answer == "a":
                points = 1
        elif answer == "A":
                points = 0          

    return(points)


if __name__ == "__main__":
    main()