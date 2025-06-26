import tkinter as tk
from gui_widgets import erstelle_widgets

einnahmen = []
ausgaben = []

def aktualisiere_anzeige(textfeld, einnahmen, ausgaben):
    textfeld.delete("1.0", tk.END)

    einnahmen_summe = sum(e[0] for e in einnahmen)
    ausgaben_summe = sum(a[0] for a in ausgaben)
    saldo = einnahmen_summe - ausgaben_summe

    textfeld.insert(tk.END, "--- Übersicht ---\n")
    textfeld.insert(tk.END, f"Einnahmen: {einnahmen_summe:.2f} €\n")
    textfeld.insert(tk.END, f"Ausgaben:  {ausgaben_summe:.2f} €\n")
    textfeld.insert(tk.END, f"Saldo:     {saldo:.2f} €\n")

    if saldo < 0:
        textfeld.insert(tk.END, "Budget Überschritten. WARNUNG!\n")

    textfeld.insert(tk.END, "\n--- Alle Einträge ---\n")
    
    if einnahmen:
        textfeld.insert(tk.END, "\nEinnahmen:\n")
        for betrag, beschreibung, kategorie in einnahmen:
            textfeld.insert(tk.END, f"  [+] {betrag:8.2f} €  –  {beschreibung} ({kategorie}\n")

    if ausgaben:
        textfeld.insert(tk.END, "\nAusgaben:\n")
        for betrag, beschreibung, kategorie in ausgaben:
            textfeld.insert(tk.END, f"  [-] {betrag:8.2f} €  –  {beschreibung} ({kategorie})\n")


def starte_gui():
    root = tk.Tk()
    root.title('Einnahmen und Ausgaben')

    textfeld = erstelle_widgets(root, einnahmen, ausgaben, aktualisiere_anzeige)

    aktualisiere_anzeige(textfeld, einnahmen, ausgaben)

    root.mainloop()

if __name__ == '__main__':
    starte_gui()