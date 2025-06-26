import json

def daten_speichern_json(einnahmen, ausgaben, dateiname='finanzen.json'):
    daten = {
        'einnahmen': einnahmen,
        'ausgaben': ausgaben
    }
    try:
        with open(dateiname, 'w', encoding='utf-8') as f:
            json.dump(daten, f, indent=4, ensure_ascii=False)
        return True
    except Exception as e:
        print(F'Fehler beim Speichern: {e}')
        return False
    
def daten_speichern_txt(einnahmen, ausgaben, dateiname='finanzen.txt'):
    try:
        with open(dateiname, 'w', encoding='utf-8') as f:
            f.write('Einnahmen: \n')
            for betrag, beschreibung in einnahmen:
                f.write(F'[+] {betrag:.2f} € - {beschreibung}\n')
            f.write('\n Ausgaben: \n')
            for betrag, beschreibung in ausgaben:
                f.write(F'[-] {betrag:.2f} € - {beschreibung}\n')
        return True
    except Exception as e:
        print(F'Fehler beim Speichern: {e}')
        return False
    
def daten_laden_json(dateiname='finanzen.json'):
    try:
        with open(dateiname, 'r', encoding='utf-8') as f:
            daten = json.load(f)
            einnahmen = daten.get('einnahmen', [])
            ausgaben = daten.get('ausgaben', [])
            return einnahmen, ausgaben
    except Exception as e:
        print(F'Fehler beim Laden: {e}')
        return [], []