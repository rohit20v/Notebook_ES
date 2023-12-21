if __name__ == '__main__':
    testo = """
    Ed è proprio da questa portentosa crema che nasce la crema al mascarpone
    base del tiramisù, prima classificata al premio Crema dell'Anno insieme
    alla nutella. Il dolce italiano per eccellenza, quello più famoso e amato,
    ma soprattutto che ha dato vita a tantissime altre versioni, anche tiramisù senza uova!
    Poi il Tiramisù alle fragole o quello alla Nutella, giusto per citarne un paio!
    Senza contare le rivisitazioni più raffinate come la crostata morbida o la torta al tiramisù.
    """

    parola_malefica1 = "Tiramisù"
    parola_malefica2 = "nutella"

    censura = "******"

    testo_censurato = (testo.replace(parola_malefica1.lower(), censura)).replace(parola_malefica2.lower(), censura)

    print(testo_censurato, "\n\tCensurate parole: ", testo_censurato.count(censura))
