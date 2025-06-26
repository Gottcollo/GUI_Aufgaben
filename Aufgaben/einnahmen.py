from utils import positiv_number

def einnahme(einnahmenliste):
    betrag = input('Einnahmenbetrag:')
    if positiv_number(betrag):
        einnahme = float(betrag)
        einnahme = round(einnahme, 2)
        einnahmenliste.append(einnahme)
        print(f'Einnahme von {einnahme:.2f} € wurden gespeichert.')
    else:
        print('Error!')