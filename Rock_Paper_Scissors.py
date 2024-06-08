import random

replay = "yes"
count = 0
win= 0
tie= 0
lost= 0

def leader_board(count,win,lost,tie):
    print("Total Numbers of Games Played: ",count)
    print("Total rounds won: ",win)
    print("Total rounds tied: ",tie)
    print("Total rounds you lost: ",lost)
    print()

def decide(choice,char):
    result= 1 if((choice=="rock" and char =="scissors")or(choice=="paper" and \
                                                          char =="rock")or (choice=="scissors" and char =="paper") ) else 2

    if result==1:
        return result
    else:
        if(char==choice):
            return 0
        else:
            return 2


def show_r(result,choice,char):
    print()
    print("You chose __ ", choice,"__")
    print("Computer Chose__ ",char,"__")
    print()
    if(result==1):
        global win
        win+=1
        print("BRAVO You WOn the Round!!")
    elif(result==2):
        global lost
        lost+=1
        print("Hard Luck You lost the round \nComputer Won...")
    else:
        global tie
        tie+=1
        print("Its a Tie between you and computer")
    print()



print("__Welocme to the Rock Paper Scissors Game__")
print("_"*56)
l = ["rock","paper","scissors"]
while replay == "yes" or replay=="y":
    choice = input("Type either of these to make your move (i.e rock , paper or scissors): ").lower()
    while(choice not in l):
        choice=input("Invalid Choice please Enter valid input: ")
    char = random.choice(l)
    result = decide(choice,char)
    show_r(result,choice,char)
    
    count += 1
    replay = input("DO You want to play again \nPress y for yes\nPress n for no \n(press L to see leaderbord)): ").lower()
    while(replay not in ("n","y","l","yes","no")):
        replay=input("ENter the valid choice (i.e y/n/L): ")
    if(replay=="l"):
        leader_board(count,win,lost,tie)
        replay = input("DO you want to play again(y for YES / n for NO : ").lower()
    if(replay in ("n","no")):
        leader_board(count,win,lost,tie)
        
