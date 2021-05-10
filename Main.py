# import tkinter as tk 
from tkinter import *

msr = Tk()

msr.title("QR Code Generator")
msr.geometry("700x500+10+20")

btn = Button(msr,text="Generate",fg="black")
btn.place(x=230,y=100)
lbl=Label(msr, text="Enter your data: ", fg='black', font=("Helvetica", 16))
lbl.place(x=60, y=50)
txtfld=Entry(msr, text="This is Entry Widget", bd=2)
txtfld.place(x=80, y=100)
canvas = Canvas(msr, width = 300, height = 300)      
canvas.pack()
msr.mainloop()