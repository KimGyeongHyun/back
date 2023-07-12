import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def find(n):

    if par[n] == n:
        return n
    return find(par[n])


def union(x, y):

    x = find(x)
    y = find(y)

    if x == y:
        return
    par[y] = x


if __name__ == "__main__":
