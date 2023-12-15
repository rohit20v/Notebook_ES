if __name__ == '__main__':
    categories = {"Ferramenta", "Ortofrutta", "Abbigliamento sportivo", "Gioielleria", "Cosmetici", "Pesce", "Alcolici",
                  "Forniture Elettriche", "Telefonia"}
    competitors = [
        ("GenerStore", {"Ortofrutta", "Abbigliamento sportivo", "Gioielleria", "Pesce", "Alcolici"}),
        ("MomentiElettrizzanti",
         {"Abbigliamento sportivo", "Videogames", "Gioielleria", "Alcolici", "Forniture Elettriche"}),
        ("TuttoEDiPiù", {"Videogames", "Gioielleria", "Pesce", "Alcolici", "Forniture Elettriche"}),
        ("ProfumoDiBuono", {"Pesce", "Alcolici", "Forniture Elettriche"}),
        ("PessimeCombo", {"Alcolici", "Telefonia"}),
    ]

    outputDict = {}
    competitor_list = [x for competitor in competitors for x in competitor[1]]

    for category in competitor_list:
        if category not in outputDict:
            countCategory = 0
            outputDict[category] = countCategory + 1
        else:
            value = outputDict[category]
            outputDict[category] = value + 1

    print(outputDict)
