if __name__ == "__main__":
    repeat = int(input())

    for i in range(repeat):
        for j in range(i+1):
            print('*', end='')
        print()

    for i in range(repeat-1, 0, -1):
        for j in range(i):
            print('*', end='')
        print()
