import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.title('Widgettraining3')
root.geometry('400x400')

foto = r'C:\Users\Sam.DESKTOP-746UJ37\Documents\RepositoryS\GUI_Aufgaben\Aufgaben\Aufgabe3.3.4\sera.png'
image = Image.open(foto)#einsetzen des bildes das ich davor als variable gegeben habe
print(F'Das Verzeichnis', os.getcwd())
image.resize([300, 300])
photo = ImageTk.PhotoImage(image)


label1 = ttk.Label(root, image= photo)#keine text option gesetzt
label1.pack()
#label1.configure(text='Hello World') //mit configure einfach option nachgesetzt 
label2 = ttk.Label(root, text='Worte')

label2.pack()



root.mainloop()