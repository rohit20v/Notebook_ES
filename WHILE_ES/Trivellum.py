if __name__ == '__main__':
    carrello = []
    pozzo = ['┼┼','┤├','┐┌', '╗╔', '║║']
    # pozzo = ['███', '▓▓▓', '▒▒▒', '░░░']

    while pozzo:
        print("Il pozzo è ", pozzo)
        block = pozzo.pop()
        carrello.extend(list(block))
        print("Trivello lo strato ", block, "e lo divido nei blocchi ", list(block))

    print("Il pozzo finale è: ", pozzo)
    print("Il carrello finale è: ", carrello)

