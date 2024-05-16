print("This is a series of questions and answers, after each question there is a 3-second wait.")

def main():

    import time

    def end():
        print(f"You've completed the series of questions with a score of {score}, Good job.")
        quit


    def countdown():
        i = 0
        while True:
            i += 1
            print(i)
            time.sleep(1)
            if i == 3:
                break

    score = 0
    question = ""
    question1 = True
    question2 = False
    question3 = False
    question4 = False
    question5 = False

    if question1 == True:
        qPrompt = input("Q1: What is the capital of France? ").lower()
        if qPrompt == "paris":
            score += 1
            print(f"Correct! Your score is: {score} points.")
            countdown()
            question2 = True
        elif qPrompt != "paris":
            print(f"Incorrect, the answer was 'Paris'. You have {score} points.")
            countdown()
            question2 = True

    elif question2 == True:
        qPrompt2 = input("Q2: What is the company with a logp of an apple? ").lower()
        if qPrompt2 == "apple":
            score += 1
            print(f"Correct! Your score is: {score} points.")
            countdown()
            question3 = True
        elif qPrompt2 != "apple":
            print(f"Incorrect, the answer was 'Apple'. You have {score} points.")
            countdown()
            question3 = True

    elif question3 == True:
        qPrompt3 = input("Q3: What is 13 + 7? ").lower()
        if qPrompt3 == "20":
            score += 1
            print(f"Correct! Your score is: {score} points.")
            countdown()
            question4 = True
        elif qPrompt3 != "20":
            print(f"Incorrect, the answer was '20'. You have {score} points.")
            countdown()
            question4 = True

    elif question4 == True:
        qPrompt4 = input("Q4: Who is the king of Britain? ").lower()
        if qPrompt4 == "king charles":
            score += 1
            print(f"Correct! Your score is: {score} points.")
            countdown()
            question5 = True
        elif qPrompt4 != "king charles":
            print(f"Incorrect, the answer was 'King Charles'. You have {score} points.")
            countdown()
            question5 = True

    elif question5 == True:
        qPrompt5 = input("Q5: What is the capital of Spain? ").lower()
        if qPrompt5 == "madrid":
            score += 1
            print(f"Correct! Your score is: {score} points. \n")
            question = "finished"
        elif qPrompt5 != "madrid":
            print(f"Incorrect, the answer was 'Madrid'. You have {score} points. \n")
            question = "finished"
    

    if question == "finished":
        end()

ask = input("Are you ready to start? (Y/N) ").lower()
if ask == "y":
    main()
elif ask == "n":
    print("Program will shut down.")
    quit()