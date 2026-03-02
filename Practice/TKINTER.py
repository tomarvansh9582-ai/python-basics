jw='vansh'
z=123456
from tkinter import *
from tkinter import messagebox
a=Tk()
def ad():
    y=eb1.get()
    if y==z:
        x=eb.get()
        y=eb1.get()
        f=open('k.txt','a')
        f.write(x)
        f.write(" ")
        f.write(y)
        f.write("\n")
        f.close()
        f=open('k.txt','r')
        print(f.read())
        f.close()
        print("LOGIN SUCCESFULLY")
        messagebox.showinfo('info','login successfully')
    else:
        print("LOGIN UNSUCCESFULL")
        messagebox.showinfo('info','try again incorrect password')   
l1=Label(a,text="USER NAME=",font=('Ariel',10),bg='green')
l1.grid(row=0,column=0)
eb=Entry(a,font=("Ariel",12),bg='orange')
eb.grid(row=0,column=9)
l2=Label(a,text="PASSWORD=",font=('Ariel',10),bg='green')
l2.grid(row=2,column=0)
eb1=Entry(a,font=("Ariel",12),show='*',bg='orange')
eb1.grid(row=2,column=9)
bt1=Button(a,text="LOG IN",bg="light green",bd=11,activebackground='blue',command=ad)
bt1.grid(row=4,column=0)
a.geometry("500x500")
a.config(bg='light blue')
a.mainloop()

