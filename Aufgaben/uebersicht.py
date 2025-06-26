def uebersicht(einnahmen, ausgaben):
    einnahmen_summe = sum(einnahmen)
    ausgaben_summe = sum(ausgaben)
    saldo = einnahmen_summe - ausgaben_summe
    print('Übersicht:')
    print(f'Einnahmen: {einnahmen_summe:.2f} €')
    print(f'Ausgaben: {ausgaben_summe:.2f} €')
    print(f'Saldo: {saldo:.2f} €')

    if saldo < 0:
        print('Budget ist überschritten! WARNUNG!')