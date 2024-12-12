from tkinter import *
import tkinter as tk
from datetime import datetime
from PIL import ImageTk


root=Tk()   
root.title("Login")

root.geometry("736x393")
img1= PhotoImage(file="C:\\Nistha\\Ctag Python\\LMS\\Downloads ⋆ Bible Symbols.png", master= root) 
img_label1= Label(root,image=img1)
img_label1.place(x=0, y=0)

l1=Label(root,text="Welcome to Library",font=("Book Antiqua",50)).pack(padx=3,pady=40)
ck1 = Checkbutton(root, text = "Member",onvalue = 1,offvalue = 0,font=("Book Antiqua",35),height =0).pack(padx=4, pady=1)
ck2=Checkbutton(root, text = "Librarian",onvalue = 1,offvalue = 0,font=("Book Antiqua",35),height =0).pack(padx=5,pady=2)
b1=Button(root,text="Exit",bg="Black",fg="White",font=("Book Antiqua",20)).pack(side=RIGHT)
#e1=Entry(root).pack()      #for input
root.mainloop()
