from tkinter import *
import tkinter as tk 

root = Tk()
root.geometry("900x1600")
root.title("Address Book")

data = []

def add():
    global data
    data.append([name.get(),number.get(),address.get(1.0,"end-1c")])
    update()

def view():
    name.set(data[int(select.curselection()[0])][0])
    number.set(data[int(select.curselection()[0])][1])
    address.delete(1.0,"end")
    address.insert(1.0,data[int(select.curselection()[0])][2])

def delete():
    del data[int(select.curselection()[0])]
    update()

def reset():
    name.set('')
    number.set('')
    address.delete(1.0,'end')

def update():
    select.delete(0,END)
    for n,p,a in data:
        select.insert(END,n)

name = StringVar()
number = StringVar()

frame1=Frame()
frame1.pack(pady=10)

frame2=Frame()
frame2.pack(pady=10)

frame3=Frame()
frame3.pack(pady=10)

Label(frame1,text="Name : ",font="arial 14").pack(side=LEFT)
Entry(frame1,textvariable=name,width=50).pack(padx=10)

Label(frame2,text="Number : ",font="arial 16").pack(side=LEFT)
Entry(frame2,textvariable=number,width=50).pack(padx=10)

Label(frame3,text="Address : ",font="arial 16").pack(side=LEFT)
address=Text(frame3,width=40,height=10)
address.pack(padx=10)

Button(root,text="Add",command=add).place(x=100,y=270)
Button(root,text="View",command=view).place(x=100,y=320)
Button(root,text="Delete",command=delete).place(x=100,y=370)
Button(root,text="Reset",command=reset).place(x=100,y=420)

scroll_bar = Scrollbar(root,orient=VERTICAL)


select=Listbox(root,yscrollcommand=scroll_bar.set,height=15,width=30)
scroll_bar.config(command=select.yview)
scroll_bar.pack(side=RIGHT,fill=Y)
select.place(x=700,y=300)
root.mainloop()
