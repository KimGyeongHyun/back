from sys import stdin


if __name__ == "__main__":
    max = 0
    high = 0
    before = 0
    n = int(stdin.readline())
    a = map(int, stdin.readline().split())

    for height in a:
        if before == 0:
            before = height
            continue
        if before < height:
            high += height - before
            if max < high:
                max = high
        else:
            high = 0
        before = height

    print(max)