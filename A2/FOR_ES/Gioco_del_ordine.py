if __name__ == '__main__':
    player1 = ["h", "b", "f", "a", "x"]
    player2 = ["e", "c", "g", "d", "z"]

    outputList = []
    for _ in player1 + player2:
        if _ in player1:
            _ = _ + "_1"
            outputList.append(_)
        elif _ in player2:
            _ = _ + "_2"
            outputList.append(_)
    print(sorted(outputList)[::-1])
