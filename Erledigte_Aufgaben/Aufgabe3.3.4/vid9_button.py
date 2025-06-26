import tkinter as tk
from tkinter import ttk

def say_hello():
    print('Hallo, Danke das du mich geklickt hast!')




root = tk.Tk()
root.geometry('600x600')

button1 = ttk.Button(root, text='Klick', padding=10, command=say_hello, state=tk.DISABLED)
#state ist normal in able/Command führt zu der def/ keine () 
button1.pack()

quit_button = ttk.Button(root, text='Programm beenden', command=root.destroy)
quit_button.pack()

for item in button1.keys():
    print(item, ':  ', button1[item])



root.mainloop()