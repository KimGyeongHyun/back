from sys import stdin
INF = int(1e9)


def floyd(g, n):
    for mid in range(1, n+1):
        for start in range(1, n+1):
            for end in range(1, n+1):
                g[start][end] = min(g[start][end], g[start][mid] + g[mid][end])


if __name__ == "__main__":
    n = int(stdin.readline())
    m = int(stdin.readline())
    g = [[INF for _ in range(n+1)] for _ in range(n+1)]

    for i in range(n+1):
        g[i][i] = 0

    for _ in range(m):
        a, b, c = map(int, stdin.readline().split())
        if c < g[a][b]:
            g[a][b] = c

    floyd(g, n)

    for i in range(1, n+1):
        for j in range(1, n+1):
            l = g[i][j]
            if l < INF:
                print(l, end=" ")
            else:
                print(0, end=" ")
        print()