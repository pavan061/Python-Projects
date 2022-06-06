
def guess_game(guess, answer):
    global score
    still_guessing = True
    attempt = 0
    while still_guessing and attempt < 3:
        if guess.lower() == answer.lower():
            score += 1
            print("Correct Answer")
            still_guessing = False
        else:
            if attempt < 2:
                guess = input("Wrong answer Keep Trying...")
            attempt += 1
    if attempt == 3:
        print("You have used all your chances :( ")
        print("The correct answer is ", answer)


score = 0
question_1  = input("Who scored more goals in a single season? ")
guess_game(question_1, "messi")
question_2 = input("who won the world cups in football history? ")
guess_game(question_2, "Brazil")
question_3 = input("Who won the most Ballon d'Or in the football history? ")
guess_game(question_3,"messi")
print(f"Your total score is :{score}")
