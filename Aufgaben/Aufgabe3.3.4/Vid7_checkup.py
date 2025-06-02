import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
 
root = tk.Tk()
root.title('Widgettraining3')
root.geometry('400x400')

style = ttk.Style()
style.theme_use('clam')
 
 
image = Image.open('Aufgaben/AufgabemitBilder/serainfullsuit.png').resize((300, 300))#oderner struktur mit angeben
photo = ImageTk.PhotoImage(image)
 
 
label1 = ttk.Label(root, image= photo)#keine text option gesetzt
label1.pack()
label1.configure(padding='50')#padding ist platz zwischen fenster
label1.configure(compound='right')
label1.configure(text='Seraphine in your Area')
label1.configure(background='red')
for item in label1.keys():
    print(item, ':  ', label1[item])
label2 = ttk.Label(root, text='Worte')
 
label2.pack()
 
 
 
root.mainloop()