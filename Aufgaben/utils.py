def positiv_number(eingabe):
    try:
        return float(eingabe) > 0
    except ValueError:
        return False