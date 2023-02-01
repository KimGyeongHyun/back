if __name__ == "__main__":
    repeat = int(input())

    for i in range(repeat, 0, -1):
        for j in range(i-1):
            print(' ', end='')
        for j in range(2*(repeat-i)+1):
            print('*', end='')
        print()