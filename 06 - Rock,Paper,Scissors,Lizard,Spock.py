from random import randint
from os import system
rock = 'rock'
paper = 'paper'
scissors = 'scissors'
lizard = 'lizard'
spock = 'spock'

options = [scissors,paper,rock,lizard,spock]

user_points = 0
pc_points = 0

games = {0: "Won", 0: "lost", 0: "Tie"}

for i in range (1,6):


    pc_choice = options[randint(0,4)]
    print ("1. %s \n2. %s \n3. %s \n4. %s \n5. %s" %(options[0],options[1],options[2],options[3],options[4]))
    user_choice = str(input("Pc decided, what do you choose? "))
    if pc_choice == "scissors":
        if user_choice in ("paper","2","lizard","4"):
            pc_points = pc_points +1
            print("You lose")
        elif user_choice == pc_choice or user_choice == "1":
            print("Tie!")
        else:
            user_points = user_points+1
            print("You won!")
        input()
    elif pc_choice == "paper":
        if user_choice in ("rock", "3", "spock", "5"):
            pc_points = pc_points + 1
            print("You lose")
        elif user_choice == pc_choice or user_choice == "2":
            print("Tie!")
        else:
            user_points = user_points + 1
            print("You won!")
        input()
    elif pc_choice == "rock":
        if user_choice in ("scissors","1","lizard","4"):
            pc_points = pc_points +1
            print("You lose")
        elif user_choice == pc_choice or user_choice == "3":
            print("Tie!")
        else:
            user_points = user_points+1
            print("You won!")
        input()
    elif pc_choice == "lizard":
        if user_choice in ("spock","5","paper","2"):
            pc_points = pc_points +1
            print("You lose")
        elif user_choice == pc_choice or user_choice == "4":
            print("Tie!")
        else:
            user_points = user_points+1
            print("You won!")
        input()
    elif pc_choice == "spock":
        if user_choice in ("scissors","1","rock","3"):
            pc_points = pc_points +1
            print("You lose")
        elif user_choice == pc_choice or user_choice == "5" :
            print("Tie!")
        else:
            user_points = user_points+1
            print("You won!")
        input()
    system("cls")

ties = 5 - pc_points - user_points
print("Game is over \nYour points: %i \nPc points: %i \nTies: %i" %(user_points, pc_points, ties))
nick = input("What is your nickname? ")
with open("leadboard.txt","a") as leadboard:
    leadboard.write("Nickname: %s | Points: %i | Loses: %i | Ties: %i \n" %(nick,user_points,pc_points,ties))
