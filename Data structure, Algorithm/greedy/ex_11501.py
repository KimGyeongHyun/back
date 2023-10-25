from sys import stdin


if __name__ == "__main__":
    t = int(stdin.readline())

    for _ in range(t):
        n = int(stdin.readline())
        l = list(map(int, stdin.readline().split()))
        c = []

        big = -1
        for i in range(len(l)-1, -1, -1):
            if big < l[i]:
                big = l[i]
            c.append(big)
        c.reverse()

        sum = 0
        for i in range(len(l)):
            sum += c[i] - l[i]

        print(sum)
