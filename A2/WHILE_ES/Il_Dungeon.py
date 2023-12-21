if __name__ == '__main__':
    cerco, caverna = 'il tesoro', ['un masso', 'una trappola', 'delle spade', 'il tesoro', 'una ragnatela',
                                   'un boleto delle tombe']

    exit = True
    print("Entro")
    i = 0
    founded = []
    while exit:
        if i < len(caverna):
            if cerco == caverna[i]:
                print(f"Che fortuna! Ho trovato {cerco}")
                exit = False
            else:
                print("Vedo", caverna[i])
                founded.append(caverna[i])
            i += 1
        else:
            print(f"Purtroppo {cerco} non c'è")
            exit = False

    print("Torno indietro")
    for i in founded[::-1]:
        print("Vedo", i)
    print("Esco")
