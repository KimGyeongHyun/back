from sys import stdin


if __name__ == "__main__":
    k = int(stdin.readline())
    l = list(map(int, stdin.readline().split()))

    for i in range(k, 0, -1):
        # print("i:", i)
        gap = 2**i
        for idx in range(2**(i-1), 2**k, gap):
            # print("idx:", idx)
            print(l[idx-1], end=' ')
        print()
