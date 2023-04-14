import sys
from collections import deque
input = sys.stdin.readline


def knight_total_move(kx, ky, lx, ly, n):

    visit = [[False for _ in range(n)] for _ in range(n)]

    d = deque()

    visit[ky][kx] = True
    d.append((ky, kx, 0))

    while d:
        y, x, c = d.popleft()
        if lx == x and ly == y:
            return c

        if x >= 1 and y >= 2 and not visit[y-2][x-1]:
            visit[y-2][x-1] = True
            d.append((y-2, x-1, c+1))
        if x >= 1 and y <= n-3 and not visit[y+2][x-1]:
            visit[y+2][x-1] = True
            d.append((y+2, x-1, c+1))

        if x >= 2 and y >= 1 and not visit[y-1][x-2]:
            visit[y-1][x-2] = True
            d.append((y-1, x-2, c+1))
        if x >= 2 and y <= n-2 and not visit[y+1][x-2]:
            visit[y+1][x-2] = True
            d.append((y+1, x-2, c+1))

        if x <= n-3 and y >= 1 and not visit[y-1][x+2]:
            visit[y-1][x+2] = True
            d.append((y-1, x+2, c+1))
        if x <= n-3 and y <= n-2 and not visit[y+1][x+2]:
            visit[y+1][x+2] = True
            d.append((y+1, x+2, c+1))

        if x <= n-2 and y >= 2 and not visit[y-2][x+1]:
            visit[y-2][x+1] = True
            d.append((y-2, x+1, c+1))
        if x <= n-2 and y <= n-3 and not visit[y+2][x+1]:
            visit[y+2][x+1] = True
            d.append((y+2, x+1, c+1))

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        kx, ky = map(int, input().split())
        lx, ly = map(int, input().split())
        print(knight_total_move(kx, ky, lx, ly, n))