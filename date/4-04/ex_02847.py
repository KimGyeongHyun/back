from sys import stdin


if __name__ == "__main__":
    n = int(stdin.readline())
    l = []
    for _ in range(n):
        l.append(int(stdin.readline()))

    count = 0
    for i in range(n-2, -1, -1):
        if l[i] >= l[i+1]:
            count += l[i] - l[i+1] + 1
            l[i] = l[i+1] - 1

    print(count)