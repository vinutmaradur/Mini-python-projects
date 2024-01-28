name = input("Type your name: ")
print("Welcome",name ,"to this adventure!")

answer = input("You are on a dirt road  , it has come to an end and you can go left or right . which way u would like to go ? ").lower()

if answer == "left":
    answer = input("You come to a river,you can walk around it or swim across ? Type walk to walk around and swim to swim across ")
    if answer == "swim":
        print("you swim across and were eaten by an alligator. ")
    elif answer == "walk":
        print("you walked for many miles,ran out of water and you lose the game.")
    else:
        print("Not a valid option. you lose.")

elif answer == "right":
    answer = input("You come to a bridge , it looks wobbly , do you want to cross it. (cross/back) ")
    if answer == "back":
        print("you go back and lose. ")
    elif answer == "cross":
        answer = input("you cross the bridge and meet a stranger . Do you talk to them(yes/no) ? ")
        if answer == "yes":
            print("You talk to the stranger and they give gold. You win.")
        elif answer == "no":
            print("You ignore the stranger and u lose.")
        else:
            print("Not a valid option. you lose. ")
    else:
        print("Not a valid option. you lose.")

else:
    print("Not a valid option.You lose.")

print("thank you! ")