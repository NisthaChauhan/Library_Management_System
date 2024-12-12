#auth_plugin='mysql_native_password'


import time
from tkinter import *

from PIL import ImageTk


root=Tk()   
root.title("Member's Main Menu")
root.geometry("1200x676")
from PIL import ImageTk

"""
img1= PhotoImage(file="C:\\Nistha\\Ctag Python\\Urban Chowk\\mainbg.png", master= root) 
img_label1= Label(root,image=img1)
img_label1.place(x=0, y=0)
"""
root.geometry("736x393")
img1= PhotoImage(file="C:\\Nistha\\Ctag Python\\LMS\\Downloads ⋆ Bible Symbols.png", master= root) 
img_label1= Label(root,image=img1)
img_label1.place(x=0, y=0)

l1=Label(root,text="Member's Main Menu",bg="#f5f5dc",font=("impact",35)).pack()#grid()
b1=Button(root,text="Book Search",bg="#f5f5dc" ,fg="black",font=("Arial Bold",18)).pack(pady=11)#grid(row=1,column=1,padx=10,pady=10)
b2=Button(root,text="Book Issue",bg="#f5f5dc" ,fg="black",font=("Arial Bold",18)).pack(pady=11)#grid(row=1,column=2,padx=10,pady=10)
b3=Button(root,text="Membership Details",bg="#f5f5dc" ,fg="black",font=("Arial Bold",18)).pack(pady=11)#grid(row=2,column=1,padx=10,pady=10)
b3=Button(root,text="Book Return",bg="#f5f5dc" ,fg="black",font=("Arial Bold",18)).pack(pady=11)#grid(row=2,column=2,p  adx=10,pady=10)
b1=Button(root,text="Exit",bg="Black",fg="White",font=("Book Antiqua",15)).pack(pady=2,side=LEFT)#grid()

#e1=Entry(root).grid()      #for input
root.mainloop()
