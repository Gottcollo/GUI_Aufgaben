import tkinter as tk
from tkinter import ttk

root = tk.Tk() #TCl interpreter wird hier gespeichert/ um widgets zu konstruieren/ ist ein Widget
root.title('Widgettraining2')
root.geometry('400x400')

label1 = tk.Label(root, text='Hallo Welt', bg='green')#tk hat nur 12 widgets und muss härter geschrieben werden
label1.pack()

label2 = ttk.Label(root, text='Kleiner')#ttk haben "klassen" dann kann man nur eine klasse changen 
#dadurch changed das auf jedem widget das diese klasse nutzt
label2.pack()

button1 = ttk.Button(root, text='Klick')
button1.pack(side='top', expand=True, fill='x')

root.mainloop()