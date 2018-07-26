from random import randint

users_choice = input("Head or Tail? \n")
users_choice = users_choice.lower()
x = randint(0,1)
if x == 0:
    x = "tail"
elif x == 1:
    x = "head"
if users_choice == x:
    print("That was "+x+", you won!")
elif users_choice != x:
    print("That wasn't "+ users_choice+" you lose :(")