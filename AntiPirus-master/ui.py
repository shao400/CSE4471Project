from tkinter import *
from antipirus import anti
import subprocess
import io
from contextlib import redirect_stdout
import login

# call login.py to make sure login in
login
if login.success == 0:
    exit()


#This is a UI framework for the antipirus codes

#tkinter window initiating variables
root = Tk() 
root.geometry("500x800") 
root.title("Malicious Python File Detection") 

#get input and loop function call antipirus program 
def Take_input():
	INPUT = inputtxt.get("1.0", "end-1c")
	f = io.StringIO()
	with redirect_stdout(f):
		anti(INPUT)
	out = f.getvalue()
	Output.insert(END, out) 

#initating text widgets

#input widget
l = Label(text = "Enter a .py file path to determine potential risk:") 
inputtxt = Text(root, height = 3, 
                width = 25, 
                bg = "light yellow") 

#output widget  
Output = Text(root, height = 50,  
              width = 60,  
              bg = "light cyan") 

#call function button  
Display = Button(root, height = 2, 
                 width = 20,  
                 text ="Scan and Detect", 
                 command = lambda:Take_input())


  
l.pack() 
inputtxt.pack() 
Display.pack() 
Output.pack()
mainloop() 