from sys import stdin


if __name__ == "__main__":
    n = int(stdin.readline())
    l = list(map(int, stdin.readline().split()))
    l.sort()

    sum = 0
    for i in range(len(l)):
        sum += l[i] * (len(l) - i)

    print(sum)