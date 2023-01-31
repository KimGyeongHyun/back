if __name__ == "__main__":
    repeat = int(input())

    for i in range(repeat, 1, -1):
        for j in range(i-1):
            print(' ', end='')
        for j in range(2*(repeat-i)+1):
            print('*', end='')
        print()

    for i in range(2 * repeat - 1):
        print('*', end='')
    print()

    for i in range(1, repeat):
        for j in range(i):
            print(' ', end='')
        for j in range(2 * (repeat-i) - 1):
            print('*', end='')
        print()

