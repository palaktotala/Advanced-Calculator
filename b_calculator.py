from tkinter import *
import math as m
import tkinter.font as font
import os

root=Tk()
root.title("Basic Calculator")

e= Entry(root, font=("Courier", 25), borderwidth="2", relief="ridge", fg="white", bg="black")
e.grid(columnspan="4", row="0", column="1", padx="10", pady="10")

def sc(operator):
	b=operator.widget
	string=b['text']
	no=e.get()
	if (no!=""): no=float(no)
	output=''
	if string=='pi':
		if no=="":
			output=str(m.pi)
		else:
			output=str(no*m.pi)
	if string=='e':
		if no=="":
			output=str(m.e)
		else:
			output=str(no*m.e)

	e.delete(0, END)
	e.insert(0, output)

def click(print_this):
	val=e.get()
	e.delete(0, END)
	e.insert(0, val+print_this)
	return

def clear():
	e.delete(0, END)
	return

def backspace():
	cur=e.get()
	length=len(cur)-1
	e.delete(length, END)

def evaluate():
	answer=e.get()
	if '^' in answer: answer=answer.replace('^','**')
	answer=eval(answer)
	e.delete(0, END)
	e.insert(0, answer)

def run2():
	root.destroy()
	os.system("C:\\Users\\PALAKT~1\\Desktop\\Projects\\Scientific-Calculator\\s_calculator.py")
	
def run3():
	root.destroy()
	os.system("C:\\Users\\PALAKT~1\\Desktop\\Projects\\Scientific-Calculator\\p_calculator.py")

menubar = Menu(root)  
menubar.add_command(label="Scientific mode", command=run2)  
menubar.add_command(label="Programmer mode", command=run3)  

root.config(menu=menubar)  

b_pfirst=Button(root,font=("Arial", 10), text="(", fg="white", bg="black", height="3", command=lambda: click("("))
b_pfirst.grid( row="1", column="2", sticky="nsew")

b_psecond=Button(root,font=("Arial", 10), text=")", fg="white", bg="black", height="3", command=lambda: click(")"))
b_psecond.grid( row="1", column="3", sticky="nsew")

b_dot=Button(root,font=("Arial", 13), text=".", fg="white", bg="black", height="3", command=lambda: click("."))
b_dot.grid( row="1", column="4", sticky="nsew")


b_Clear=Button(root,font=("Arial", 10), text="Clear", fg="white", bg="Red", height="3", command=lambda: clear())
b_Clear.grid( row="1", column="1", sticky="nsew")

b_Back=Button(root,font=("Arial", 10), text="Back", fg="white", bg="Red", height="3", command=lambda: backspace())
b_Back.grid( row="3", column="1", sticky="nsew")

b_div=Button(root,font=("Arial", 10), text="/", fg="white", bg="black", height="3", command=lambda: click("/"))
b_div.grid( row="3", column="4", sticky="nsew")


b_seven=Button(root,font=("Arial", 10), text="7", fg="white", bg="grey", height="3", command=lambda: click("7"))
b_seven.grid( row="4", column="1", sticky="nsew")

b_eight=Button(root,font=("Arial", 10), text="8", fg="white", bg="grey", height="3", command=lambda: click("8"))
b_eight.grid( row="4", column="2", sticky="nsew")

b_nine=Button(root,font=("Arial", 10), text="9", fg="white", bg="grey", height="3", command=lambda: click("9"))
b_nine.grid( row="4", column="3", sticky="nsew")

b_mult=Button(root,font=("Arial", 13), text="*", fg="white", bg="black", height="3", command=lambda: click("*"))
b_mult.grid( row="4", column="4", sticky="nsew")


b_four=Button(root,font=("Arial", 10), text="4", fg="white", bg="grey", height="3", command=lambda: click("4"))
b_four.grid( row="5", column="1", sticky="nsew")

b_five=Button(root,font=("Arial", 10), text="5", fg="white", bg="grey", height="3", command=lambda: click("5"))
b_five.grid( row="5", column="2", sticky="nsew")

b_six=Button(root,font=("Arial", 10), text="6", fg="white", bg="grey", height="3", command=lambda: click("6"))
b_six.grid( row="5", column="3", sticky="nsew")

b_sub=Button(root,font=("Arial", 13), text="-", fg="white", bg="black", height="3", command=lambda: click("-"))
b_sub.grid( row="5", column="4", sticky="nsew")


b_one=Button(root,font=("Arial", 10), text="1", fg="white", bg="grey", height="3", command=lambda: click("1"))
b_one.grid( row="6", column="1", sticky="nsew")

b_two=Button(root,font=("Arial", 10), text="2", fg="white", bg="grey", height="3", command=lambda: click("2"))
b_two.grid( row="6", column="2", sticky="nsew")

b_three=Button(root,font=("Arial", 10), text="3", fg="white", bg="grey", height="3", command=lambda: click("3"))
b_three.grid( row="6", column="3", sticky="nsew")

b_add=Button(root,font=("Arial", 13), text="+", fg="white", bg="black", height="3", command=lambda: click("+"))
b_add.grid( row="6", column="4", sticky="nsew")


b_zero=Button(root,font=("Arial", 10), text="0", fg="white", bg="grey", height="3", command=lambda: click("0"))
b_zero.grid( row="7", column="2", sticky="nsew")

b_equal=Button(root,font=("Arial", 12), text="=", fg="black", bg="yellow", height="3", command=lambda: evaluate())
b_equal.grid( row="7", column="3", sticky="nsew")

b_pi=Button(root,font=("Arial", 10), text="pi", fg="white", bg="black", height="3")
b_pi.bind("<Button-1>",sc)
b_pi.grid( row="3", column="2", sticky="nsew")

b_e=Button(root,font=("Arial", 10), text="e", fg="white", bg="black", height="3")
b_e.bind("<Button-1>",sc)
b_e.grid( row="3", column="3", sticky="nsew")

root.mainloop()
