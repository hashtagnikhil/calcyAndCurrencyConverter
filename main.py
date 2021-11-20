import tkinter
import os
from tkinter import *


from tkinter import messagebox

root = tkinter.Tk()
root.geometry("700x400")
root.title("Dashboard")
root.configure(background="cornflowerblue")

frame = LabelFrame(root,text="Click on the Button given below:",padx=90,pady=90,bg="cornflowerblue",bd="10",cursor="dot",font=("cooper",15,"bold",UNDERLINE,"italic"),fg="black")
frame.pack(padx=15,pady=15)

def selection():

 os.system('currency.py')
def selection1():

 os.system('calculator.py')




btn1=Button(frame,text="Calculator",fg="black",font=("Times New Roman",20,"bold"),bg="cornsilk",command=selection1)
btn1.pack()
btn2=Button(frame,text="Currency Converter",font=("Times New Roman",20,"bold"),bg="cornsilk",command=selection)
btn2.pack()



root.mainloop()