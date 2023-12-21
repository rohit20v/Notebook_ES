if __name__ == '__main__':
    testo = "CiAo QuEsTo E' uN TeStO sToRto"
    outputTesto = ""
    for letter in testo:
        if letter.islower():
            outputTesto = outputTesto + letter.upper()
        elif letter.isupper():
            outputTesto = outputTesto + letter.lower()
        elif letter.isspace():
            outputTesto = outputTesto + " "

    print(outputTesto)
