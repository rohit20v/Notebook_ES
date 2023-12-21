if __name__ == '__main__':
    circuit = [('condensatore', 8), ('resistenza', 4), ('led', 5), ('diodo', 1), ('trasduttore', 2),
               ('transistor', 12), ('sensore', 3), ('solenoide', 10)]
    print([x[0] for x in circuit if (x[1] > 4)])
