from tkinter import *

root = Tk()
root.geometry('300x300')
root.title("Mad Libs")

Label(root,text="MadLibs Generator",font='arial 20 bold').pack()
Label(root,text="Click any one: ",font='arial 15 bold').place(x=40,y=80)

def madlibs1():
    name = input("Your name : ")
    dob = input("Your dob : ")
    place = input("Your city : ")
    print(f"My name is {name}.I was born on {dob} in {place}.")

def madlibs2():
    animal = input("Enter the animal name : ")
    eats = input("What animal eats : ")
    print(f"Animal name is {animal}.{animal} eats {eats}.")

Button(root,text="Introduction",font="arial 15",command=madlibs1,bg="ghost white").place(x=70,y=120)
Button(root,text="Animal Maker",font="arial 15",command=madlibs2,bg="ghost white").place(x=70,y=180)
root.mainloop()