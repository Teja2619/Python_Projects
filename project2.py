import random
items=["rock","paper","scissor"]
score_system=0
score_you=0
for i in range(1,6):
    choice=input("enter one option from rock or scissor or paper:  ")
    system=random.choice(items)
    print(f"your choice is {choice} and system's choice is {system}")

    try:
        if choice==system:
            print("your match is tied")
        elif choice=="rock" :
            if system=="scissor":
                print("rock wins so you wins the game")
                score_you+=10
            else :
                print("scissor wins so you lost the game")
                score_system+=10
        elif choice=="paper" :
            if system=="scissor":
                print("scissor wins so you lost the game")
                score_system+=10
            else :
                print("paper wins so you won the game")
                score_you+=10
        elif choice=="scissor" :
            if system=="paper":
                print("scissor wins so you wins the game")
                score_you+=10
            else :
                print("rock wins so you lost the game")
                score_system+=10
    except:
        print("invalid option")
print(f"system score = {score_system}")
print(f"your score = {score_you}")

if score_system<score_you:
    print("you are the winner of contest")
elif score_you<score_system:
    print("you lost the contest")
else:
    print("oops! both are winners or you can play again")
