import timeit
start = timeit.timeit()
print("hello")



print("Welcome To My Quiz Game")

playing=input("Do you want play?")

if playing !="yes":
    quit()
print("That' Nice! Let's play")

score=0

answer=input("What does IT stand for?:")
if answer.lower() == "ınformation technology":
    print("CORRECT! Congratulations!")
    score+=1
else:
    print("incorrect...")
    score-=1


answer=input("What does YBS stand for?:")
if answer.lower() == "yönetim bilişim sistemleri":
    print("CORRECT! Congratulations!")  
    score+=1  
else:
    print("incorrect...")
    score-=1


answer=input("What does RAM stand for?:")
if answer.lower() == "random acces memory":
    print("CORRECT! Congratulations! Lets play 2. tour")
    score+=1
else:
    print("incorrect...")
    score-=1


answer=input("What does LAN stand for?:")
if answer.lower() == "local area network":
    print("CORRECT! Congratulations!")
    score+=5
else:
    print("incorrect...")
    score-=1


answer=input("What does WAN stand for?:")
if answer.lower() == "wide area network":
    print("CORRECT! Congratulations!")
    score+=5
else:
    print("incorrect...")
    score-=1

print("you got"  + str(score) + "question correct")
print("you got"  + str((score/4)*100) + "%.")


end = timeit.timeit()
print(end - start)