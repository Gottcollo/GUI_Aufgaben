import tkinter as tk
from tkinter import messagebox
from speichern import daten_speichern_json, daten_speichern_txt, daten_laden_json

def erstelle_widgets(root, einnahmen, ausgaben, aktualisiere_anzeige):

    betrag_var = tk.StringVar()
    beschreibung_var = tk.StringVar()
    kategorie_entry = tk.Entry(root)

    tk.Label(root, text='Kategorie:').grid(row=2, column=0, padx=5, pady=5)
    kategorie_entry.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(root, text='Betrag in Euro: ').grid(row=0, column=0, padx=5, pady=5)
    betrag_entry = tk.Entry(root, textvariable=betrag_var)
    betrag_entry.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(root, text='Beschreibung: ').grid(row=1, column=0, padx=5, pady=5)
    beschreibung_entry = tk.Entry(root, textvariable=beschreibung_var)
    beschreibung_entry.grid(row=1, column=1, padx=5, pady=5)

    textfeld = tk.Text(root, height=10, width=50)
    textfeld.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')

    root.grid_rowconfigure(4, weight=1)
    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(1, weight=1)

    def einnahme_hinzufuegen():
        try:
            betrag = float(betrag_var.get())
            beschreibung = beschreibung_entry.get()
            kategorie = kategorie_entry.get() or 'Allgemein'
            if betrag <= 0:
                raise ValueError('Betrag muss positiv sein.')
            einnahmen.append((betrag, beschreibung_var.get(), kategorie))
            aktualisiere_anzeige(textfeld, einnahmen, ausgaben)
            betrag_entry.delete(0, tk.END)
            beschreibung_entry.delete(0, tk.END)
            kategorie_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror('Fail, einen positiven Betrag eingeben')

    def ausgabe_hinzufuegen():
        try:
            betrag = float(betrag_var.get())
            beschreibung = beschreibung_entry.get()
            kategorie = kategorie_entry.get() or 'Allgemein'
            if betrag <= 0:
                raise ValueError('Betrag muss positiv sein.')
            ausgaben.append((betrag, beschreibung_var.get(), kategorie))
            aktualisiere_anzeige(textfeld, einnahmen, ausgaben)
            betrag_entry.delete(0, tk.END)
            beschreibung_entry.delete(0, tk.END)
            kategorie_entry.delete(0, tk.END)
        except ValueError:
            messagebox.showerror('Fail, einen positiven Betrag eingeben')

    def speichern_json():
        if daten_speichern_json(einnahmen, ausgaben):
            messagebox.showinfo('Erfolg', 'Daten erfolgreich gespeichert als JSON.')
        else:
            messagebox.showerror('Fehler')

    def speichern_txt():
        if daten_speichern_txt(einnahmen, ausgaben):
            messagebox.showinfo('Erfolg', 'Daten erfolgreich gespeichert als TXT.')
        else:
            messagebox.showerror('Fehler')

    def laden_json():
        geladen_einnahmen, geladen_ausgaben = daten_laden_json()
        einnahmen.clear()
        einnahmen.extend(geladen_einnahmen)
        ausgaben.clear()
        ausgaben.extend(geladen_ausgaben)
        aktualisiere_anzeige(textfeld, einnahmen, ausgaben)
        messagebox.showinfo('Erfolg, Daten geladen')

    tk.Button(root, text='Einnahme hinzufügen', command=einnahme_hinzufuegen).grid(row=3, column=0, padx=5, pady=5)
    tk.Button(root, text='Ausgabe hinzufügen', command=ausgabe_hinzufuegen).grid(row=3, column=1, padx=5, pady=5)
    tk.Button(root, text='Als JSON speichern', command=speichern_json).grid(row=4, column=0, padx=5, pady=5)
    tk.Button(root, text='Als TXT speichern', command=speichern_txt).grid(row=4, column=1, padx=5, pady=5)

    textfeld.grid(row=5, column=0, columnspan=2, padx=5, pady=5, sticky='nsew')
    tk.Button(root, text='Daten Laden', command=laden_json).grid(row=6, column=0, columnspan=2, padx=5, pady=5)


    return textfeld