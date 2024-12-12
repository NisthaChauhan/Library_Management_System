import time
from tkinter import *

from PIL import ImageTk


root=Tk()   
root.title("Issue")
root.geometry("1200x676")

root.geometry("736x393")
img1= PhotoImage(file="C:\\Nistha\\Ctag Python\\LMS\\Downloads ⋆ Bible Symbols.png", master= root) 
img_label1= Label(root,image=img1)
img_label1.place(x=0, y=0)

l1=Label(root,text="Issue",bg="#f5f5dc",font=("impact",35)).grid(padx=10,pady=10,row=1,column=1)#grid()

l2=Label(root,text="Book Title :",bg="#f5f5dc",font=("impact",15)).grid(padx=10,pady=10,row=2,column=2)#grid()
#l3=Label(root,text=title,bg="#f5f5dc",font=("impact",15)).grid(padx=10,pady=10,row=2,column=3)#TITLE VARIBLE

l4=Label(root,text="Author's Name :",bg="#f5f5dc",font=("impact",15)).grid(padx=10,pady=10,row=3,column=2)#grid()
#l5=Label(root,text=author,bg="#f5f5dc",font=("impact",15)).grid(padx=10,pady=10,row=3,column=3)#AUTHOR VARIABLE

l6=Label(root,text="Genre :",bg="#f5f5dc",font=("impact",15)).grid(padx=10,pady=10,row=4,column=2)#grid()
#l7=Label(root,text=genre,bg="#f5f5dc",font=("impact",10)).grid(padx=10,pady=10,row=4,column=3)#GENRE VARIABLE

#l9=Label(root,text=status,bg="#f5f5dc",font=("impact",10)).grid(padx=10,pady=10,row=5,column=3)#STATUS VARIABLE

#l10=Label(root,text="Issue :",bg="#f5f5dc",font=("impact",15),command=issue).grid(padx=10,pady=10,row=6,column=2)#grid()
l11=Label(root,text="Exit",bg="#f5f5dc",font=("impact",15)).grid(padx=10,pady=10,row=6,column=3)#GENRE VARIABLE


#NOTEs
l12=Label(root,text="Exit",bg="#f5f5dc",font=("impact",15)).grid(padx=10,pady=10,row=6,column=3)#GENRE VARIABLE
l13=Label(root,text="Exit",bg="#f5f5dc",font=("impact",15)).grid(padx=10,pady=10,row=6,column=3)#GENRE VARIABLE


root.mainloop()