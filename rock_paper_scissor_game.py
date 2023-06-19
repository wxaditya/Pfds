import random

opt=["rock", "paper", "scissors"]

comchoice=random.choice(opt)

uscore=cscore=0
while (uscore<3 and cscore<3):
    uchoice= input("Choose rock, paper, or scissors: ").lower()
    print("User choice: ",uchoice)
    print("Computer choice:", comchoice)

    if uchoice == comchoice:
        print("It's a tie!")
        print("scores remains same")
        print("User score : ",uscore)
        print("computer score : ",cscore)
        continue
    elif uchoice == "rock":
        if comchoice == "paper":
            print("Computer wins!")
            cscore+=1
            print("User score : ",uscore)
            print("computer score : ",cscore)
            
        else:
            print("You win!")
            uscore+=1
            print("User score : ",uscore)
            print("computer score : ",cscore)
    elif uchoice == "paper":
        if comchoice == "scissors":
            print("Computer wins!")
            cscore+=1
            print("User score : ",uscore)
            print("computer score : ",cscore)
        else:
            print("You win!")
            uscore+=1
            print("User score : ",uscore)
            print("computer score : ",cscore)
    elif uchoice == "scissors":
        if comchoice == "rock":
            print("Computer wins!")
            cscore+=1
            print("User score : ",uscore)
            print("computer score : ",cscore)
        else:
            print("You win!")
            uscore+=1
            print("User score : ",uscore)
            print("computer score : ",cscore)
    else:
        print("Invalid input. Please choose rock, paper, or scissors.")
if uscore==3 and cscore!=3:
    print("finals score are :")
    print("user score : ",uscore)
    print("computer score : ", cscore)
    print("user score 3 first, win the game")
else :
    print("finals score are :")
    print("user score : ",uscore)
    print("computer score : ", cscore)
    
    print("computer score 3 first ,win the game")

