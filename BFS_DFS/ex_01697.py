import sys
from collections import deque

input = sys.stdin.readline


def get_time(n, k):
    # BFS

    # 방문 여부
    visit = [False for _ in range(100001)]
    visit[n] = True     # 수빈이가 있는 곳은 방문한 곳

    d = deque()         # BFS 를 위한 데크
    d.append((n, 0))    # 수빈이위 위치, 지난 시간

    while d:
        x, c = d.popleft()

        # 동생을 찾았다면 지난 시간을 반환
        if x == k:
            return c

        # 가능한 모든 조건 안에서 BFS 수행
        if x >= 1 and not visit[x-1]:
            visit[x-1] = True
            d.append((x-1, c+1))
        if x <= 99999 and not visit[x+1]:
            visit[x+1] = True
            d.append((x+1, c+1))
        if x <= 50000 and not visit[2*x]:
            visit[2*x] = True
            d.append((2*x, c+1))


if __name__ == "__main__":
    n, k = map(int, input().split())
    print(get_time(n, k))