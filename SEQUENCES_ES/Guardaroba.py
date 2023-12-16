if __name__ == '__main__':
    indumenti = ['cappotti', 'giacconi', 'mantelli', 'ventine']
    capi = [9, 5, 7, 3]

    [print("ci sono", indumenti[1], indumenti[0]) for indumenti in zip(indumenti, capi)]
