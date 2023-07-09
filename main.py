import time
import random

print("==================================== Welcome to Rock, Paper, Sciccors!!! ====================================")
print("All you have to do is choose 1 out of the 3 options and the computer will also choose 1 of the 3 options")
print("Whoever wins the round gets a point. Whoever has the most points at the end of 5 rounds wins. Best of luck!")
roundNumber = 0
userScore = 0
computerScore = 0
while roundNumber < 5:
    def AIChoice():
        choices = ["Rock", "Paper", "Sciccors"]
        return random.choice(choices)
    
    
    answer = input("What do you choose? ")
    aiChoice = AIChoice()
    print("ROCK")
    time.sleep(1)
    print("PAPER")
    time.sleep(1)
    print("SCICCORS")
    time.sleep(1)
    print("SHOOT")
    time.sleep(1)
    print(answer)
    print(aiChoice)

    if answer == "Rock" and aiChoice == "Rock":
        print("Dang it, a tie. Better luck next time!")
        userScore+=1
        computerScore+=1
        roundNumber +=1
    elif answer == "Rock" and aiChoice == "Paper":
        print("Computer wins!")
        computerScore+=1
        roundNumber +=1
    elif answer == "Rock" and aiChoice == "Sciccors":
        print("User Wins!")
        userScore+=1
        roundNumber +=1
    elif answer == "Paper" and aiChoice == "Rock":
        print("User Wins!")
        userScore+=1
        roundNumber +=1
    elif answer == "Paper" and aiChoice == "Paper":
        print("Dang it a tie. Better luck next time!")
        userScore+=1
        computerScore+=1
        roundNumber +=1
    elif answer == "Paper" and aiChoice == "Sciccors":
        print("Computer wins!")
        computerScore+=1
        roundNumber +=1
    elif answer == "Sciccors" and aiChoice == "Rock":
        print("Computer Wins!")
        computerScore+=1
        roundNumber +=1
    elif answer == "Sciccors" and aiChoice == "Paper":
        print("User wins!")
        userScore+=1
        roundNumber +=1
    elif answer == "Sciccors" and aiChoice == "Sciccors":
        print("Dang it, a tie. Better luck next time!")
        computerScore+=1
        roundNumber +=1
        userScore+=1
    else:
        print("Please enter a choice of rock, paper, or sciccors.")


print("======================================================")
print("The game as concluded, here are the scores:")
print("User: " + str(userScore))
print("Computer: " + str(computerScore))

if userScore > computerScore:
    print("User wins!")
elif computerScore > userScore:
    print("Computer Wins!")

