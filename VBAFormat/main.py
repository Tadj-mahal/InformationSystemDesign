import tkinter as tk
from tkinter import ttk
import math

def get_function():
	f = combobox.get()
	x = float(x_inp.get())
	if f == "sqrt(1/(e^(x)))":
		y = math.sqrt(1/(math.exp(x)))
	elif f == "sqrt(e^(1/(x)))":
		if x != 0:
			y = math.sqrt(math.exp(1/(x)))
		else:
			y = 'Value not correct!'
	elif f == "1/(sqrt(e^(x)))":
		y = 1/(math.sqrt(math.exp(x)))
	elif f == "1/(e^(sqrt(x)))":
		y = 1/(math.exp(math.sqrt(x)))
	elif f == "e^(sqrt(1/(x)))":
		if x != 0 and x > 0:
			y = math.exp(math.sqrt(1/(x)))
		else:
			y = 'Value not correct!'
	elif f == "e^(1/(sqrt(x)))":
		if x >= 0:
			y = math.exp(1/(math.sqrt(x)))
		else:
			y = 'Value not correct!'
	else:
		y = x
	code = f"Function F(x As Double) '= {f})\nOn Error Go To E_Catch\nF = {f})\nExit Function\nE_Catch:\nSelect Case Err.Number\nCase 11\nCall MsgBox(\"Division by 0\",, \"Error)\nCase 5\nCall MsgBox(\"Square root of negative number\",, \"Error\")\nCase Else\nCall MsgBox(\"Error: \" & Err.Number & \"\" & Err.Description)\nEnd Select\nErr.Raise Err.Number\nEnd Function\n\nSub TestF()\nDim x As Double\nx = Application.InputBox()\nDebug.Print(F(x))\nEnd Sub"
	label_val.config(text=f"f(x) = {y}")
	vba_code.insert(tk.END, code)

root = tk.Tk()
root.title("VBA-Format")

input_frame = tk.Frame(root)
input_frame.pack(side=tk.LEFT)

f1 = "sqrt"
f2 = "1/"
f3 = "e^"
functions = [f1+"("+f2+"("+f3+"(x)))", f1+"("+f3+"("+f2+"(x)))", f2+"("+f1+"("+f3+"(x)))", f2+"("+f3+"("+f1+"(x)))", f3+"("+f1+"("+f2+"(x)))", f3+"("+f2+"("+f1+"(x)))"]
label_function = tk.Label(input_frame, text="Choose function:")
combobox = ttk.Combobox(input_frame,values=functions)

label_x = tk.Label(input_frame, text="Input value of variable:")
x_inp = tk.Entry(input_frame)
get_y = tk.Button(input_frame, text="Calculate", command=get_function)


label_x.grid(row=1, column=0)
x_inp.grid(row=1, column=1)
label_function.grid(row=2, column=0)
combobox.grid(row=2, column=1)
get_y.grid(row=3, column=0)


output_frame = tk.Frame(root)
output_frame.pack(side=tk.RIGHT)

label_val = tk.Label(output_frame)
vba_code = tk.Text(output_frame, height = 20, width = 52)

label_val.grid(row=1, column=0)
vba_code.grid(row=2,column=0)

root.mainloop()