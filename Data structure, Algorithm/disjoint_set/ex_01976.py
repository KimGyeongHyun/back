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


def trip_success():
    parent = find(trip[0]-1)
    for i in range(1, len(trip)):
        t_parent = find(trip[i]-1)
        if parent != t_parent:
            return "NO"
    return "YES"


if __name__ == "__main__":
    n = int(input())
    m = int(input())
    par = [i for i in range(n)]

    for i in range(n):
        l = list(map(int, input().split()))
        for j in range(i+1, n):
            if l[j] == 1:
                union(i, j)
    trip = list(map(int, input().split()))
    print(trip_success())