import tkinter as tk

root = tk.Tk()

label1 = tk.Label(root, text='Hallo Welt') #immer auf das Fatherfenster setzen
button1 = tk.Button(root, text='Klick') #habe einfach einen button hinzugefügt 
label1.pack() #muss "verpackt" werden damit es genutzt wird 
button1.pack()
root.mainloop()

print('Air')

