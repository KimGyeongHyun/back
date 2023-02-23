from sys import stdin


if __name__ == "__main__":
    max = 0
    index = 0
    for i in range(1, 10):
        a = int(stdin.readline())
        if i == 1:
            max = a
            index = i
            continue
        if max < a:
            max = a
            index = i

    print(max)
    print(index)