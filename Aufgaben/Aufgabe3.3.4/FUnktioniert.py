import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
 
root = tk.Tk()
root.title('Widgettraining3')
root.geometry('600x600')
 
 
image = Image.open('bilder/sera1.png').resize((300, 300))#ordner angeben/DUMMES VID HAT ES MIR NCIHT GESAGT
photo = ImageTk.PhotoImage(image)
 
 
label1 = ttk.Label(root, image= photo)#keine text option gesetzt
label1.pack()
label1.configure(padding='50')#padding ist platz zwischen fenster
label1.configure(compound='right')
label1.configure(text='Seraphine in your Area')
#label1.configure(text='Hello World') //mit configure einfach option nachgesetzt
label2 = ttk.Label(root, text='Worte')
 
label2.pack()
 
 
 
root.mainloop()