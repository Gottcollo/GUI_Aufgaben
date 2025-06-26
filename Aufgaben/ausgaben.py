from utils import positiv_number

def ausgabe(ausgabenliste):
    betrag = input('Ausgabenbetrag:')
    if positiv_number(betrag):
        ausgabe = float(betrag)
        ausgabe = round(ausgabe, 2)
        ausgabenliste.append(ausgabe)
        print(f'Ausgabe von {ausgabe:.2f} € wurden gespeichert.')
    else:
        print('Error!')