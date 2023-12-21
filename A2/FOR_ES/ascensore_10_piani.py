if __name__ == '__main__':
    while True:
        start = int(input('Enter the starting floor numba: '))
        end = int(input('Enter the ending floor numba: '))
        if start in range(10+1) and end in range(10+1):
            for i in range(end, start - 1, -1): print(i)
            print("DING!")
            break
        else:
            print('Invalid input')
