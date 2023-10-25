import sys
from collections import deque
input = sys.stdin.readline

def tomato_prev_day(n, m, l):

    # BFS

    visit = [[False for _ in range(m)] for _ in range(n)]   # 방문 여부

    d = deque()     # BFS 활용을 위한 데크

    for x in range(m):
        for y in range(n):
            if l[y][x] == 1:
                visit[y][x] = True
                d.append((y, x, 0))     # y, x 좌표, 지난 일수

    day = 0     # 모든 토마토가 익은 일수
    while d:
        y, x, c = d.popleft()
        # BFS 순회에 따라 마지막으로 순회한 토마토는 마지막으로 익는 토마토
        # 마지막으로 익는 토마토의 지난 일수를 모든 토마토가 익은 일수 변수에 저장
        day = c

        # 조건에 따라 모든 토마토 순회
        if x >= 1 and not visit[y][x-1] and l[y][x-1] == 0:
            visit[y][x-1] = True
            d.append((y, x-1, c+1))
        if x <= m-2 and not visit[y][x+1] and l[y][x+1] == 0:
            visit[y][x+1] = True
            d.append((y, x+1, c+1))
        if y >= 1 and not visit[y-1][x] and l[y-1][x] == 0:
            visit[y-1][x] = True
            d.append((y-1, x, c+1))
        if y <= n-2 and not visit[y+1][x] and l[y+1][x] == 0:
            visit[y+1][x] = True
            d.append((y+1, x, c+1))

    # 토마토가 있는 곳에 순회하지 못했다면 -1 반환
    for x in range(m):
        for y in range(n):
            if not visit[y][x] and l[y][x] != -1:
                return -1

    # 모든 토마토가 익은 일수 반환
    return day


if __name__ == "__main__":
    m, n = map(int, input().split())
    l = []
    for _ in range(n):
        l.append(list(map(int, input().split())))

    print(tomato_prev_day(n, m, l))