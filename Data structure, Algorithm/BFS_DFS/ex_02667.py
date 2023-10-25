import sys
from collections import deque

input = sys.stdin.readline


def print_home_count(n, l):
    # BFS

    visit = [[False for _ in range(n)] for _ in range(n)]   # 방문 여부
    res = []    # 단지 별 집 갯수 저장 리스트

    for i in range(n):
        for j in range(n):
            # 좌표 모두 탐색

            # 이미 탐색한 집이라면 넘어감
            if not l[i][j] or visit[i][j]:
                continue

            c = 1           # 단지 내 집 갯수
            d = deque()     # BFS 를 위한 데크

            visit[i][j] = True  # 탐색 처리
            d.append((i, j))    # 좌표 저장

            while d:
                y, x = d.popleft()

                # 붙어있는 모든 집을 방문 처리하고 while 문을 빠져나옴
                if x >= 1 and l[y][x-1] == 1 and not visit[y][x-1]:
                    c += 1
                    visit[y][x-1] = True
                    d.append((y, x-1))
                if x <= n-2 and l[y][x+1] == 1 and not visit[y][x+1]:
                    c += 1
                    visit[y][x+1] = True
                    d.append((y, x+1))
                if y >= 1 and l[y-1][x] == 1 and not visit[y-1][x]:
                    c += 1
                    visit[y-1][x] = True
                    d.append((y-1, x))
                if y <= n-2 and l[y+1][x] == 1 and not visit[y+1][x]:
                    c += 1
                    visit[y+1][x] = True
                    d.append((y+1, x))

            # 단지 내 집의 개수를 res 에 추가
            res.append(c)

    res.sort()
    print(len(res))
    for num in res:
        print(num)


if __name__ == "__main__":
    n = int(input())
    l = []
    for _ in range(n):
        line = list(map(int, input()[:-1]))
        l.append(line)

    print_home_count(n, l)

