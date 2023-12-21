if __name__ == '__main__':
    frase = ['Por', 'el', 'suelo', 'camina', 'mi', 'pueblo']
    print([tuple((y + 1) for y in range(len(x)))for x in frase])
