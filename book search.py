#auth_plugin='mysql_native_password'


import time
from tkinter import *
from PIL import ImageTk


root=Tk()   
root.title("Book Search")
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

l1=Label(root,text="Search",bg="#f5f5dc",font=("impact",35)).grid(padx=10,pady=10,row=1,column=1)#grid()

l2=Label(root,text="Book Title :",bg="#f5f5dc",font=("impact",15)).grid(padx=10,pady=10,row=2,column=2)#grid()
e1=Entry(root).grid(padx=10,pady=10,row=2,column=3)      #for input

l3=Label(root,text="Author's Name :",bg="#f5f5dc",font=("impact",15)).grid(padx=10,pady=10,row=3,column=2)#grid()
e2=Entry(root).grid(padx=10,pady=10,row=3,column=3)      #for input

l4=Label(root,text="Genre :",bg="#f5f5dc",font=("impact",15)).grid(padx=10,pady=10,row=4,column=2)#grid()
e3=Entry(root).grid(padx=10,pady=10,row=4,column=3)      #for input

l5=Label(root,text="Search",bg="#f5f5dc",font=("impact",10)).grid(padx=10,pady=10,row=5,column=3)#grid()

l6=Label(root,text="Chack Status",bg="#f5f5dc",font=("impact",10),command=check_status).grid(padx=10,pady=10,row=5,column=3)#grid()

root.mainloop()