import random

user_wins = 0
computer_wins = 0

options =["rock","paper","scissors"]

while True:
    user_input = input("Type rock/paper/scissors or Q to quit :")
    if user_input == "q" :
        break

    if user_input not in options :
        continue

    random_number=random.randint(0 , 2)     #taş:0 , kağıt:1, makas:2
    computer_pick = options[random_number]
    print("Computer Picked",computer_pick)

    if user_input == "rock" and computer_pick == "scissors":
        print("-YOU WON-")
        user_wins+=1

    elif user_input == "paper" and computer_pick =="rock":
        print("-YOU WON-")
        user_wins+=1

    elif user_input == "scissors" and computer_pick == "paper":    
        print("-YOU WON-")
        user_wins+=1

    else:
        print("-YOU LOST-")
        computer_wins +=1


print("-YOU WON-",user_wins,"times.")
print("-THE COMPUTER WON-",computer_wins,"times.")
print("-GOOD BYE-")