import tkinter as tk
import mysql.connector as m

def exit_application():
    root.destroy()

def issue_book():
    try:
        pas="nistha"
        db="library"
        con=m.connect(host="localhost",user="root",passwd=pas,database=db,auth_plugin='mysql_native_password')
        cur=con.cursor()
        t="books"
        qry="insert into masalahouse values('"+str(bid)+"','"+title+"','"+author+"','"+status+"')"
        cur.execute()
        con.commit()
    except Exception as e:
        print(f"Error: {e}")
root = tk.Tk()   
root.title("Issue")
root.geometry("736x393")

# Your image code
img1 = tk.PhotoImage(file="C:\\Nistha\\Ctag Python\\LMS\\Downloads ⋆ Bible Symbols.png", master=root) 
img_label1 = tk.Label(root, image=img1)
img_label1.place(x=0, y=0)

# Your labels and buttons
l1 = tk.Label(root, text="Issue", bg="#f5f5dc", font=("impact", 35))
l1.grid(padx=10, pady=10, row=1, column=1)

l2 = tk.Label(root, text="Book Title:", bg="#f5f5dc", font=("impact", 15))
l2.grid(padx=10, pady=10, row=2, column=2)

l4 = tk.Label(root, text="Author's Name:", bg="#f5f5dc", font=("impact", 15))
l4.grid(padx=10, pady=10, row=3, column=2)

l6 = tk.Label(root, text="Genre:", bg="#f5f5dc", font=("impact", 15))
l6.grid(padx=10, pady=10, row=4, column=2)

issue_button = tk.Button(root, text="Issue", bg="#f5f5dc", font=("impact", 15), command=issue_book)
issue_button.grid(padx=10, pady=10, row=6, column=2)

exit_button = tk.Button(root, text="Exit", bg="#f5f5dc", font=("impact", 15), command=exit_application)
exit_button.grid(padx=10, pady=10, row=6, column=3)

# Notes and other labels...

root.mainloop()
