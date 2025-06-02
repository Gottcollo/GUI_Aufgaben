import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
 
root = tk.Tk()
root.title('Widgettraining3')
root.geometry('400x400')
 
 
image = Image.open('Aufgaben/AufgabemitBilder/sera.png').resize((300, 300))#oderner struktur mit angeben
photo = ImageTk.PhotoImage(image)
 
 
label1 = ttk.Label(root, image= photo)#keine text option gesetzt
label1.pack()
#label1.configure(text='Hello World') //mit configure einfach option nachgesetzt
label2 = ttk.Label(root, text='Worte')
 
label2.pack()
 
 
 
root.mainloop()