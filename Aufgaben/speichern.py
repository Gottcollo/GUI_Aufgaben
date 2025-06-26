import json

def daten_speichern_json(einnahmen, ausgaben, dateiname='finanzen.json'):
    daten = {
        'einnahmen': [
            {'betrag': betrag, 'beschreibung': beschreibung, 'kategorie': kategorie}
            for betrag, beschreibung, kategorie in einnahmen
        ],
        'ausgaben': [
            {'betrag': betrag, 'beschreibung': beschreibung, 'kategorie': kategorie}
            for betrag, beschreibung, kategorie in ausgaben
        ]
    }
    try:
        with open(dateiname, 'w', encoding='utf-8') as f:
            json.dump(daten, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(f'Fehler beim Speichern: {e}')
        return False

    
def daten_speichern_txt(einnahmen, ausgaben, dateiname='finanzen.txt'):
    try:
        with open(dateiname, 'w', encoding='utf-8') as f:
            f.write('Einnahmen:\n')
            for betrag, beschreibung, kategorie in einnahmen:
                f.write(f'[+] {betrag:.2f} € - {beschreibung} ({kategorie})\n')

            f.write('\nAusgaben:\n')
            for betrag, beschreibung, kategorie in ausgaben:
                f.write(f'[-] {betrag:.2f} € - {beschreibung} ({kategorie})\n')

        return True
    except Exception as e:
        print(f'Fehler beim Speichern: {e}')
        return False

    
def daten_laden_json(dateiname='finanzen.json'):
    try:
        with open(dateiname, 'r', encoding='utf-8') as f:
            daten = json.load(f)
            einnahmen = [
                (eintrag['betrag'], eintrag['beschreibung'], eintrag.get('kategorie', 'Allgemein'))
                for eintrag in daten.get('einnahmen', [])
            ]
            ausgaben = [
                (eintrag['betrag'], eintrag['beschreibung'], eintrag.get('kategorie', 'Allgemein'))
                for eintrag in daten.get('ausgaben', [])
            ]
            return einnahmen, ausgaben
    except Exception as e:
        print(f'Fehler beim Laden: {e}')
        return [], []
