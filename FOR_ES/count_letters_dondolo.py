if __name__ == '__main__':
    words= ["ssss","eee","rrrrrr","sssssss"]
    string = ",".join(words)

    firstLetters = []
    dict = {}
    for word in words:
        if word[0] not in firstLetters: firstLetters.append(word[0])

    for letter in firstLetters: dict[letter] = string.count(letter)
    print(dict)