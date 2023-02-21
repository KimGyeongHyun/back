if __name__ == "__main__":
    repeat = int(input())

    for i in range(repeat):
        for j in range(i):
            print(' ', end='')
        for j in range(2 * (repeat-i) - 1):
            print('*', end='')
        print()