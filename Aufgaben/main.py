from einnahmen import einnahme
from ausgaben import ausgabe
from uebersicht import uebersicht
from utils import positiv_number
from menue import menue


einnahmen = []
ausgaben = []



def main():
    while True:
        menue()
        wahl = input('Bitte wählen Sie eine Option (1-4): ')
        
        if wahl == '1':
            einnahme(einnahmen)
        elif wahl == '2':
            ausgabe(ausgaben)
        elif wahl == '3':
            uebersicht(einnahmen, ausgaben)
        elif wahl == '4':
            print('Beendet.')
            break
        else:
            print('Ungültige Eingabe. Wähle eine Option zwischen 1 und 4.')

if __name__ == '__main__':
    main()