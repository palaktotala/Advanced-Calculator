from tkinter import *
import tkinter.font as font
import tkinter.messagebox
import os
import winsound

root=Tk()
root.title("Programmer Calculator")
e= Entry(root, font=("Courier", 25), borderwidth="2", relief="ridge", fg="white", bg="black")
e.grid(columnspan="5", row="1", column="1")

frequency = 2500  # Set Frequency To 2500 Hertz
duration = 1000  # Set Duration To 1000 ms == 1 second

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

def evaluate(v1,v2):
	x = v1.get()
	y = v2.get()
	
	if((x=="1") and (y=="1")):
		try:
			answer=e.get()
			answer=bin(int(answer, 2))
			e.delete(0, END)
			e.insert(0, answer)
		except Exception as ex:
			winsound.Beep(frequency, duration)
			e.delete(0,END)
			e.insert(0, "ERROR")

	if((x=="2") and (y=="2")):
		try:
			answer=e.get()
			answer=int(answer)
			e.delete(0, END)
			e.insert(0, answer)
		except Exception as ex:
			winsound.Beep(frequency, duration)
			e.delete(0,END)
			e.insert(0, "ERROR")	

	if((x=="3") and (y=="3")):
		try:
			answer=e.get()
			answer=hex(int(answer, 16))
			e.delete(0, END)
			e.insert(0, answer)
		except Exception as ex:
			winsound.Beep(frequency, duration)
			e.delete(0,END)
			e.insert(0, "ERROR")

	if((x=="4") and (y=="4")):
		try:
			answer=e.get()
			answer=oct(int(answer, 8))
			e.delete(0, END)
			e.insert(0, answer)
		except Exception as ex:
			winsound.Beep(frequency, duration)
			e.delete(0,END)
			e.insert(0, "ERROR")

	if((x=="1") and (y=="2")):
		answer=e.get()
		try: 
			answer=int(answer, 2)
			e.delete(0, END)
			e.insert(0, answer)
		except Exception as ex:
			winsound.Beep(frequency, duration)
			e.delete(0,END)
			e.insert(0, "ERROR")

	if((x=="1") and (y=="3")):
		answer=e.get()
		try:
			answer=hex(int(answer, 2))
			e.delete(0, END)
			e.insert(0, answer)
		except Exception as ex:
			winsound.Beep(frequency, duration)
			e.delete(0,END)
			e.insert(0, "ERROR")

	if((x=="1") and (y=="4")):
		answer=e.get()
		try:
			answer=oct(int(answer, 2))
			e.delete(0, END)
			e.insert(0, answer)
		except Exception as ex:
			winsound.Beep(frequency, duration)
			e.delete(0,END)
			e.insert(0, "ERROR")

	if((x=="2") and (y=="1")):
		answer=e.get()
		try:
			answer=bin(int(answer))
			e.delete(0, END)
			e.insert(0, answer)
		except Exception as ex:
			winsound.Beep(frequency, duration)
			e.delete(0,END)
			e.insert(0, "ERROR")

	if((x=="2") and (y=="3")):
		answer=e.get()
		try:
			answer=hex(int(answer))
			e.delete(0, END)
			e.insert(0, answer)
		except Exception as ex:
			winsound.Beep(frequency, duration)
			e.delete(0,END)
			e.insert(0, "ERROR")

	if((x=="2") and (y=="4")):
		answer=e.get()
		try:
			answer=oct(int(answer))
			e.delete(0, END)
			e.insert(0, answer)
		except Exception as ex:
			winsound.Beep(frequency, duration)
			e.delete(0,END)
			e.insert(0, "ERROR")

	if((x=="3") and (y=="1")):
		answer=e.get()
		try:
			answer=bin(int(answer, 16))
			e.delete(0, END)
			e.insert(0, answer)
		except Exception as ex:
			winsound.Beep(frequency, duration)
			e.delete(0,END)
			e.insert(0, "ERROR")

	if((x=="3") and (y=="2")):
		answer=e.get()
		try:
			answer=int(answer, 16)
			e.delete(0, END)
			e.insert(0, answer)
		except Exception as ex:
			winsound.Beep(frequency, duration)
			e.delete(0,END)
			e.insert(0, "ERROR")

	if((x=="3") and (y=="4")):
		answer=e.get()
		try:
			answer=oct(int(answer, 16))
			e.delete(0, END)
			e.insert(0, answer)
		except Exception as ex:
			winsound.Beep(frequency, duration)
			e.delete(0,END)
			e.insert(0, "ERROR")

	if((x=="4") and (y=="1")):
		answer=e.get()
		try:
			answer=bin(int(answer, 8))
			e.delete(0, END)
			e.insert(0, answer)
		except Exception as ex:
			winsound.Beep(frequency, duration)
			e.delete(0,END)
			e.insert(0, "ERROR")

	if((x=="4") and (y=="2")):
		answer=e.get()
		try:
			answer=int(answer, 8)
			e.delete(0, END)
			e.insert(0, answer)
		except Exception as ex:
			winsound.Beep(frequency, duration)
			e.delete(0,END)
			e.insert(0, "ERROR")

	if((x=="4") and (y=="3")):
		answer=e.get()
		try:
			answer=hex(int(answer, 8))
			e.delete(0, END)
			e.insert(0, answer)
		except Exception as ex:
			winsound.Beep(frequency, duration)
			e.delete(0,END)
			e.insert(0, "ERROR")
		
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

b_A=Button(root,font=("Arial", 10), text="A", fg="white", bg="grey", height="3", command=lambda: click("A"))
b_A.grid( row="3", column="4", sticky="nsew")

b_B=Button(root,font=("Arial", 10), text="B", fg="white", bg="grey", height="3", command=lambda: click("B"))
b_B.grid( row="3", column="5", sticky="nsew")

b_C=Button(root,font=("Arial", 10), text="C", fg="white", bg="grey", height="3", command=lambda: click("C"))
b_C.grid( row="4", column="4", sticky="nsew")

b_D=Button(root,font=("Arial", 10), text="D", fg="white", bg="grey", height="3", command=lambda: click("D"))
b_D.grid( row="4", column="5", sticky="nsew")

b_E=Button(root,font=("Arial", 10), text="E", fg="white", bg="grey", height="3", command=lambda: click("E"))
b_E.grid( row="5", column="4", sticky="nsew")

b_F=Button(root,font=("Arial", 10), text="F", fg="white", bg="grey", height="3", command=lambda: click("F"))
b_F.grid( row="5", column="5", sticky="nsew")

b_eval=Button(root,font=("Arial", 10), text="=", fg="white", bg="grey", height="3", command=lambda: evaluate(v1,v2))
b_eval.grid(columnspan="2",row="6", column="4", sticky="nsew")

v1 = StringVar(root, "1")
v2 = StringVar(root, "2")

Rb=Radiobutton(root, text = "Binary", variable = v1, value = "1", indicator = 0, fg="black", bg="light blue", height="3")
Rb.grid(columnspan="2",row="7", column="1", sticky="nsew")

Rd=Radiobutton(root, text = "Decimal", variable = v1, value = "2", indicator = 0, fg="black", bg="light blue", height="3")
Rd.grid(columnspan="3",row="7", column="3", sticky="nsew")

Rh=Radiobutton(root, text = "Hexa", variable = v1, value = "3", indicator = 0, fg="black", bg="light blue", height="3")
Rh.grid(columnspan="2",row="8", column="1", sticky="nsew")

Ro=Radiobutton(root, text = "Octal", variable = v1, value = "4", indicator = 0, fg="black", bg="light blue", height="3")
Ro.grid(columnspan="3",row="8", column="3", sticky="nsew")

Rb1=Radiobutton(root, text = "Binary", variable = v2, value = "1", indicator = 0, fg="black", bg="light blue", height="3")
Rb1.grid(columnspan="2",row="9", column="1", sticky="nsew")

Rd1=Radiobutton(root, text = "Decimal", variable = v2, value = "2", indicator = 0, fg="black", bg="light blue", height="3")
Rd1.grid(columnspan="3",row="9", column="3", sticky="nsew")

Rh1=Radiobutton(root, text = "Hexa", variable = v2, value = "3", indicator = 0, fg="black", bg="light blue", height="3")
Rh1.grid(columnspan="2",row="10", column="1", sticky="nsew")

Ro1=Radiobutton(root, text = "Octal", variable = v2, value = "4", indicator = 0, fg="black", bg="light blue", height="3")
Ro1.grid(columnspan="3",row="10", column="3", sticky="nsew")



root.mainloop()

