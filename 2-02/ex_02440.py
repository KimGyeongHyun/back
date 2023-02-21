if __name__ == "__main__":
    repeat = int(input())

    for i in range(repeat, 0, -1):
        for j in range(i):
            print('*', end='')
        print()