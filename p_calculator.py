from tkinter import *
import tkinter.font as font
import tkinter.messagebox
import os

root=Tk()
root.title("Programmer Calculator")
e= Entry(root, font=("Courier", 25), borderwidth="2", relief="ridge", fg="white", bg="black")
e.grid(columnspan="5", row="1", column="1")

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

def B2D():
	answer=e.get()
	try: 
		answer=int(answer, 2)
		e.delete(0, END)
		e.insert(0, answer)
	except Exception as ex:
		tkinter.messagebox.showerror("Error", "Invalid conversion")


def B2H():
	answer=e.get()
	try:
		answer=hex(int(answer, 2))
		e.delete(0, END)
		e.insert(0, answer)
	except Exception as ex:
		tkinter.messagebox.showerror("Error", "Invalid input")

def B2O():
	answer=e.get()
	try:
		answer=oct(int(answer, 2))
		e.delete(0, END)
		e.insert(0, answer)
	except Exception as ex:
		tkinter.messagebox.showerror("Error", "Invalid input")

def D2B():
	answer=e.get()
	try:
		answer=bin(int(answer))
		e.delete(0, END)
		e.insert(0, answer)
	except Exception as ex:
		tkinter.messagebox.showerror("Error", "Invalid input")

def D2H():
	answer=e.get()
	try:
		answer=hex(int(answer))
		e.delete(0, END)
		e.insert(0, answer)
	except Exception as ex:
		tkinter.messagebox.showerror("Error", "Invalid input")

def D2O():
	answer=e.get()
	try:
		answer=oct(int(answer))
		e.delete(0, END)
		e.insert(0, answer)
	except Exception as ex:
		tkinter.messagebox.showerror("Error", "Invalid input")

def H2B():
	answer=e.get()
	try:
		answer=bin(int(answer, 16))
		e.delete(0, END)
		e.insert(0, answer)
	except Exception as ex:
		tkinter.messagebox.showerror("Error", "Invalid input")

def H2D():
	answer=e.get()
	try:
		answer=int(answer, 16)
		e.delete(0, END)
		e.insert(0, answer)
	except Exception as ex:
		tkinter.messagebox.showerror("Error", "Invalid input")

def H2O():
	answer=e.get()
	try:
		answer=oct(int(answer, 16))
		e.delete(0, END)
		e.insert(0, answer)
	except Exception as ex:
		tkinter.messagebox.showerror("Error", "Invalid input")

def O2B():
	answer=e.get()
	try:
		answer=bin(int(answer, 8))
		e.delete(0, END)
		e.insert(0, answer)
	except Exception as ex:
		tkinter.messagebox.showerror("Error", "Invalid input")

def O2D():
	answer=e.get()
	try:
		answer=int(answer, 8)
		e.delete(0, END)
		e.insert(0, answer)
	except Exception as ex:
		tkinter.messagebox.showerror("Error", "Invalid input")

def O2H():
	answer=e.get()
	try:
		answer=hex(int(answer, 8))
		e.delete(0, END)
		e.insert(0, answer)
	except Exception as ex:
		tkinter.messagebox.showerror("Error", "Invalid input")

def run2():
	root.destroy()
	os.system("C:\\Users\\PALAKT~1\\Desktop\\Projects\\Scientific-Calculator\\b_calculator.py")
	
def run3():
	root.destroy()
	os.system("C:\\Users\\PALAKT~1\\Desktop\\Projects\\Scientific-Calculator\\s_calculator.py")

menubar = Menu(root)  
menubar.add_command(label="Basic mode", command=run2)  
menubar.add_command(label="Scientific mode", command=run3)  

root.config(menu=menubar) 

b_Clear=Button(root,font=("Arial", 10), text="Clear", fg="white", bg="Red", height="3", command=lambda: clear())
b_Clear.grid( row="3", column="1", sticky="nsew")

b_Back=Button(root,font=("Arial", 10), text="Back", fg="white", bg="Red", height="3", command=lambda: backspace())
b_Back.grid( row="3", column="2", sticky="nsew")

b_seven=Button(root,font=("Arial", 10), text="7", fg="white", bg="grey", height="3", command=lambda: click("7"))
b_seven.grid( row="4", column="1", sticky="nsew")

b_eight=Button(root,font=("Arial", 10), text="8", fg="white", bg="grey", height="3", command=lambda: click("8"))
b_eight.grid( row="4", column="2", sticky="nsew")

b_nine=Button(root,font=("Arial", 10), text="9", fg="white", bg="grey", height="3", command=lambda: click("9"))
b_nine.grid( row="4", column="3", sticky="nsew")

b_four=Button(root,font=("Arial", 10), text="4", fg="white", bg="grey", height="3", command=lambda: click("4"))
b_four.grid( row="5", column="1", sticky="nsew")

b_five=Button(root,font=("Arial", 10), text="5", fg="white", bg="grey", height="3", command=lambda: click("5"))
b_five.grid( row="5", column="2", sticky="nsew")

b_six=Button(root,font=("Arial", 10), text="6", fg="white", bg="grey", height="3", command=lambda: click("6"))
b_six.grid( row="5", column="3", sticky="nsew")

b_one=Button(root,font=("Arial", 10), text="1", fg="white", bg="grey", height="3", command=lambda: click("1"))
b_one.grid( row="6", column="1", sticky="nsew")

b_two=Button(root,font=("Arial", 10), text="2", fg="white", bg="grey", height="3", command=lambda: click("2"))
b_two.grid( row="6", column="2", sticky="nsew")

b_three=Button(root,font=("Arial", 10), text="3", fg="white", bg="grey", height="3", command=lambda: click("3"))
b_three.grid( row="6", column="3", sticky="nsew")

b_zero=Button(root,font=("Arial", 10), text="0", fg="white", bg="grey", height="3", command=lambda: click("0"))
b_zero.grid( row="3", column="3", sticky="nsew")

b_zero=Button(root,font=("Arial", 10), text="A", fg="white", bg="grey", height="3", command=lambda: click("A"))
b_zero.grid( row="3", column="4", sticky="nsew")

b_zero=Button(root,font=("Arial", 10), text="B", fg="white", bg="grey", height="3", command=lambda: click("B"))
b_zero.grid( row="3", column="5", sticky="nsew")

b_zero=Button(root,font=("Arial", 10), text="C", fg="white", bg="grey", height="3", command=lambda: click("C"))
b_zero.grid( row="4", column="4", sticky="nsew")

b_zero=Button(root,font=("Arial", 10), text="D", fg="white", bg="grey", height="3", command=lambda: click("D"))
b_zero.grid( row="4", column="5", sticky="nsew")

b_zero=Button(root,font=("Arial", 10), text="E", fg="white", bg="grey", height="3", command=lambda: click("E"))
b_zero.grid( row="5", column="4", sticky="nsew")

b_zero=Button(root,font=("Arial", 10), text="F", fg="white", bg="grey", height="3", command=lambda: click("F"))
b_zero.grid( row="5", column="5", sticky="nsew")

b_equal=Button(root,font=("Arial", 12), text="B2D", fg="black", bg="yellow", height="3", command=lambda: B2D())
b_equal.grid( row="6", column="4", sticky="nsew")

b_equal=Button(root,font=("Arial", 12), text="B2H", fg="black", bg="yellow", height="3", command=lambda: B2H())
b_equal.grid( row="6", column="5", sticky="nsew")

b_equal=Button(root,font=("Arial", 12), text="B2O", fg="black", bg="yellow", height="3", command=lambda: B2O())
b_equal.grid( row="7", column="1", sticky="nsew")

b_equal=Button(root,font=("Arial", 12), text="D2B", fg="black", bg="yellow", height="3", command=lambda: D2B())
b_equal.grid( row="7", column="2", sticky="nsew")

b_equal=Button(root,font=("Arial", 12), text="D2H", fg="black", bg="yellow", height="3", command=lambda: D2H())
b_equal.grid( row="7", column="3", sticky="nsew")

b_equal=Button(root,font=("Arial", 12), text="D2O", fg="black", bg="yellow", height="3", command=lambda: D2O())
b_equal.grid( row="7", column="4", sticky="nsew")

b_equal=Button(root,font=("Arial", 12), text="H2B", fg="black", bg="yellow", height="3", command=lambda: H2B())
b_equal.grid( row="7", column="5", sticky="nsew")

b_equal=Button(root,font=("Arial", 12), text="H2D", fg="black", bg="yellow", height="3", command=lambda: H2D())
b_equal.grid( row="8", column="1", sticky="nsew")

b_equal=Button(root,font=("Arial", 12), text="H2O", fg="black", bg="yellow", height="3", command=lambda: H2O())
b_equal.grid( row="8", column="2", sticky="nsew")

b_equal=Button(root,font=("Arial", 12), text="O2B", fg="black", bg="yellow", height="3", command=lambda: O2B())
b_equal.grid( row="8", column="3", sticky="nsew")

b_equal=Button(root,font=("Arial", 12), text="O2D", fg="black", bg="yellow", height="3", command=lambda: O2D())
b_equal.grid( row="8", column="4", sticky="nsew")

b_equal=Button(root,font=("Arial", 12), text="O2H", fg="black", bg="yellow", height="3", command=lambda: O2H())
b_equal.grid( row="8", column="5", sticky="nsew")


root.mainloop()

