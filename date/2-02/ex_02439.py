if __name__ == "__main__":
    repeat = int(input())

    for i in range(1, repeat+1):
        for j in range(repeat-i):
            print(' ', end='')
        for j in range(i):
            print('*', end='')
        print()