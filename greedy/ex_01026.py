from sys import stdin


if __name__ == "__main__":
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    b = list(map(int, stdin.readline().split()))

    a.sort()
    b.sort()
    b.reverse()

    sum = 0
    for i in range(n):
        sum += a[i] * b[i]

    print(sum)