print("Welcome to my computer quiz!")

playing  = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("Okay ! let's play")
score = 0

answer = input("What does cpu stand for? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else :
    print("Incorrect") 

answer = input("What does gpu stand for? ")
if answer.lower() == "Graphics processing unit":
    score += 1
    print("correct!")
else :
    print("Incorrect")

answer = input("What does ram stand for? ")
if answer.lower() == "Random access memory":
    score += 1
    print("correct!")
else :
    print("Incorrect")

answer = input("What does psu stand for? ")
if answer.lower() == "power supply":
    score +=1 
    print("correct!")
else :
    print("Incorrect")

print("You got " + str(score) + " questions correct!")
print("you got " + str((score / 4)*100) + "%.")