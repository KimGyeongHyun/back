import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n = int(input())
    l = []
    for _ in range(n):
        l.append(tuple(map(int, input().split())))

    l = sorted(l, key=lambda x : (x[0], x[1]))

    for item in l:


