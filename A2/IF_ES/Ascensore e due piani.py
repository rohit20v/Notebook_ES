if __name__ == '__main__':
    # piano_utente = 'terra'; piano_ascensore = 'rialzato'
    # piano_utente = 'rialzato'; piano_ascensore = 'terra'
    # piano_utente = 'terra'; piano_ascensore = 'terra'
    piano_utente = 'rialzato'; piano_ascensore = 'rialzato'

    if piano_utente == piano_ascensore:
        print("DING!")
    elif piano_utente.lower() == 'terra':
        print("rialzato")
        print("terra")
        print("DING!")
    elif piano_ascensore.lower() == 'terra':
        print("terra")
        print("rialzato")
        print("DING!")