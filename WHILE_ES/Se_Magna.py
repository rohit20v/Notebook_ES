if __name__ == '__main__':
    panini, burgers = 8, 5

    while panini > 0 and burgers > 0:
        print(f"Servito un panino: {panini - 1} panini rimanenti, {burgers - 1} burger rimanenti")
        panini -= 1
        burgers -= 1

    if panini > burgers: print("Avanzano", panini, "panini")
    elif burgers > panini: print("Avanzano", burgers, "burger")
    else: print("ERR")
