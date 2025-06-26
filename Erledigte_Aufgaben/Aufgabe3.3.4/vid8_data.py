import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('600x600')

text_variable =  tk.StringVar() #eine variable erzeugt die behandelbar ist
text_variable.set('Das ist der neue Text') #set um die variable nun zu setzen
nummer_variable = tk.IntVar()#Integer variable 
nummer_variable.set(10)
nummer2_variable = tk.DoubleVar()#float variable
nummer2_variable.set(10.5)
boolean_variable = tk.BooleanVar()#boolean (1,0) True and False
boolean_variable.set(True)



label1 = ttk.Label(root, textvariable=text_variable)
label1.pack()
label2 = ttk.Label(root, textvariable=nummer_variable)
text_variable.set('Aktualisierter Text') #frischer neuer Labelsatz
nummer_variable.set(20)
label2.pack()
nummer2_variable.set(40.54)
label3 = ttk.Label(root, textvariable=nummer2_variable)
label3.pack()
label4 = ttk.Label(root, textvariable=boolean_variable)
label4.pack()


root.mainloop()