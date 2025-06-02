import tkinter as tk

root = tk.Tk() #TCl interpreter wird hier gespeichert/ um widgets zu konstruieren/ ist ein Widget

label1 = tk.Label(root, text='Hallo Welt') #immer auf das Fatherfenster setzen
button1 = tk.Button(root, text='Klick') #habe einfach einen button hinzugefügt 
label1.pack() #muss "gepackt auf Father" werden damit es genutzt wird 
button1.pack() #bewegung im fenster/sonst nur generiert / Für festere Bewegung mehr informationen
root.mainloop()

print('Air')

