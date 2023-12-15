if __name__ == '__main__':
    monte = [90, 40, 50, 20, 60, 7, 3, 4, 9, 8]
    half = len(monte) // 2
    list1 = monte[:half]
    list2 = monte[half:]
    outputList = sorted(list1) + sorted(list2)[::-1]
    print(outputList)