from sys import stdin


if __name__ == "__main__":
    n = int(stdin.readline())
    m = int(stdin.readline())

    min = 0
    sum = 0

    for i in range(1, 10001):
        sq = i**2
        if n <= sq <= m:
            if min == 0:
                min = sq
            sum += sq

    if min == 0:
        print(-1)
    else:
        print(sum)
        print(min)
