import random
x = input("Do you wanna play?(y/n)")
while(x=='y'):
    user = int(input("Enter 0 for snake, 1 for water, 2 for gun"))
    computer=  random.randint(0,2)
    if(computer==user):
        print("You:",user)
        print("Computer:",computer)
        print("Its a draw!!")
    elif(computer==0 and user==1):
        print("You:",user)
        print("Computer:",computer)
        print("You lose!!")
    elif(computer==0 and user==2):
        print("You:",user)
        print("Computer:",computer)
        print("You win!!!")
    elif(computer==1 and user==2):
        print("You:",user)
        print("Computer:",computer)
        print("You lose!!")
    elif(computer==1 and user==0):
        print("You:",user)
        print("Computer:",computer)
        print("You Win!!")
    elif(computer==2 and user==0):
        print("You:",user)
        print("Computer:",computer)
        print("You lose!!")
    elif(computer==2 and user==1):
        print("You:",user)
        print("Computer:",computer)
        print("You Win!!")
    print("Wanna play again?(y/n)")
    x= input()