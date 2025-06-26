import tkinter as tk
from tkinter import ttk

def print_entry_input():#def für rückgabe in der GUI
    ttk.Label(root, text=entry1.get()).pack()

def delete_input():
    entry1.delete(0, tk.END)#mit tk.END ist es der letzmögliche Indexansatz


root = tk.Tk()
root.geometry('600x600')

entry1 = ttk.Entry(root, width=40)
entry1.pack()
entry1.insert(0, 'Eingabebereich')#einfach bereich was einschreiben/indexzahl zeigt an wo es startet


button1 = ttk.Button(root, text='eingabe', command=print_entry_input)
button1.pack()
button2 = ttk.Button(root, text='Lösche input', command=delete_input)
button2.pack()


for item in entry1.keys():
    print(item, ': ' , entry1[item])




root.mainloop()