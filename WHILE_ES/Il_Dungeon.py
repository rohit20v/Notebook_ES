if __name__ == '__main__':
    cerco, caverna = 'il tesoro', ['un masso', 'una trappola', 'delle spade', 'il tesoro', 'una ragnatela',
                                   'un boleto delle tombe']

    exit = True
    print("Entro")
    i = 0
    found = ""
    while exit:
        if i < len(caverna):
            if cerco == caverna[i]:
                print(f"Che fortuna! Ho trovato {cerco}")
                found = cerco
                exit = False
            else:
                print("Vedo", caverna[i])
            i += 1
        else:
            print(f"Purtroppo {cerco} non c'è")
            exit = False

    while i >= 0:
        if cerco == found:
            print("Torno indietro")
            while i > 0:
                i -= 1
                print("Vedo", caverna[i])
            print("Esco")
        else:
            print("Torno indietro")
            while i > 0:
                i -= 1
                print("Vedo", caverna[i])
            print("Esco")
        i -= 1
