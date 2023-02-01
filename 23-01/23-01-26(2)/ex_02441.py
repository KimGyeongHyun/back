if __name__ == "__main__":
    repeat = int(input())

    for i in range(0, repeat):
        for j in range(i):
            print(' ', end='')
        for j in range(repeat-i):
            print('*', end='')
        print()