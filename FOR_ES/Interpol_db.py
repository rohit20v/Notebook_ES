if __name__ == '__main__':
    nomi = ['hacKnights', 'Cult  of  Cobra', 'unsafe\nKreW']
    dossier = ['hack.odt', 'cobra.odt', 'unsafe.docx']

    db = dict(zip(nomi, dossier))
    ricerca = 'HacKnights'
    for key in db:
        if ricerca.casefold() == key.casefold():
            print(ricerca, "è documentato nel dossier", db[key])
