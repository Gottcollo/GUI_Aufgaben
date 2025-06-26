import tkinter as tk

root = tk.Tk() #TCl interpreter wird hier gespeichert/ um widgets zu konstruieren/ ist ein Widget
root.title('Hier steht der Titel')
root.geometry('400x400')#start größe für Fatherfenster
root.minsize(width=250, height=250)#minimale größe
root.maxsize(width=600, height=600)#maximale größe
root.resizable(width=False, height=True)
label1 = tk.Label(root, text='Hallo Welt') #immer auf das Fatherfenster setzen
button1 = tk.Button(root, text='Klick') #habe einfach einen button hinzugefügt 
label1.pack() #muss "gepackt auf Father" werden damit es genutzt wird 
button1.pack() #bewegung im fenster/sonst nur generiert / Für festere Bewegung mehr informationen
root.mainloop()

print('Air')

