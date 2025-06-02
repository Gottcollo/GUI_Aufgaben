import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os
 
root = tk.Tk()
root.title('Widgettraining3')
root.geometry('400x400')
print("SCRIPT:", __file__)
print("CWD   :", os.getcwd())
print("EXISTS?", os.path.exists('sera.png'))
image_path = os.path.join(os.path.dirname(__file__), 'sera.png') #os benutzt um direkt das zu finden/sucht nur 
image = Image.open(image_path).resize((300, 300)) 
photo = ImageTk.PhotoImage(image)
 
label1 = ttk.Label(root, text='Das ist mein Bild', image= photo, compound='bottom', padding ='5')#keine text option gesetzt
label1.pack()
label1.configure(font=('Gothic'))
for item in label1.keys():
    print(item, ':  ', label1[item])
#label1.configure(text='Hello World') //mit configure einfach option nachgesetzt
label2 = ttk.Label(root, text='Worte')
 
label2.pack()
 
root.mainloop()
