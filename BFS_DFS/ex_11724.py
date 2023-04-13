import sys
from collections import deque

input = sys.stdin.readline


def get_connected_component_number(n, l):
    # BFS

    visit = [False for _ in range(n+1)]     # 방문 여부
    c = 0   # 요소 개수

    # 요소 개수를 세기 위한 반복문
    for i in range(1, n+1):

        # 이미 방문한 노드라면 요소 개수를 올리지 않고 다음 노드로 넘어감
        if visit[i]:
            continue

        d = deque()     # BFS 를 위한 데크
        visit[i] = True     # 해당 노드 방문 처리
        d.append(i)

        while d:    # 해당 노드와 연결된 모든 노드를 방문 처리하고 탈출
            num = d.popleft()
            for j in range(1, n+1):
                if not visit[j] and l[num][j]:
                    visit[j] = True
                    d.append(j)

        # 요소 갯수 + 1
        c += 1

    return c


if __name__ == "__main__":
    n, m = map(int, input().split())
    # 그래프 생성
    l = [[False for _ in range(n+1)] for _ in range(n+1)]
    for _ in range(m):
        u, v = map(int, input().split())
        l[u][v] = True
        l[v][u] = True

    print(get_connected_component_number(n, l))
