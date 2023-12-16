if __name__ == '__main__':
    # ginevra = True; merlino = True; morgana = False
    # ginevra = False; merlino = False; morgana = True
    # ginevra = False; merlino = True; morgana = False
    # ginevra = False; merlino = True; morgana = True
    # ginevra = True; merlino = False; morgana = False
    # ginevra = True; merlino = False; morgana = True
    # ginevra = True; merlino = True; morgana = False
    ginevra = True; merlino = True; morgana = True

    if ginevra and merlino and morgana:
        print("Sono tutti veri cavalieri")
    elif ginevra or merlino or morgana:
        print("C'è almeno un vero cavaliere")
    else:
        print("Non c'è nessun vero cavaliere")
