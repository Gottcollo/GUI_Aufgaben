import tkinter as tk

root = tk.Tk() #TCl interpreter wird hier gespeichert/ um widgets zu konstruieren/ ist ein Widget
root.title('Widgettraining')
root.geometry('400x400')
label1 = tk.Label(root, text='Hallo Welt', bg='green')# bg setzt denn hintergrund
label1.pack(side='top',expand=True)#layoutmanager argumente mit pack default site value ist Top
label2 = tk.Label(root, text='Katzekraft', bg = 'Red')
label2.pack(side='top', expand=True, fill='both')
#site values sind 'bottom', 'left', 'right'
root.mainloop()