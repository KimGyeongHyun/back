import sys
from collections import deque


input = sys.stdin.readline

# DFS
# 깊이 우선 탐색 (Depth)
# 스택 자료구조나 재귀 함수로 구현
# 1. 탐색 시작 노드를 스택에 삽입, 방문 처리
# 2. 스택 최상단 노드에 방문하지 않은 인접한 노드 있으면
#     그 노드를 스택에 넣고 방문 처리
#     방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드 꺼냄
# 3. 2번 과정을 수행할 수 없을 때까지 반복
#
# 기본적인 방문 기준은 번호가 낮은 인접 노드 순서
# (상황에 따라 달라질 수 있음)

# BFS
# 너비 우선 탐색 (Breadth)
# 큐 자료구조
# 1. 탐색 시작 노드를 큐에 삽입, 방문 처리
# 2. 큐에서 노드를 꺼낸 뒤
#     해당 노드의 인접 노드 중 방문하지 않은 노드를 모두 큐에 삽입, 방문 처리
# 3. 2번 과정을 수행할 수 없을 때까지 반복


def DFS(l, node, n, visit):
    visit[node-1] = True
    print(node, end=" ")

    tl = l[node-1]
    for i in range(n):
        if not visit[i] and tl[i] == 1:
            DFS(l, i+1, n, visit)


def BFS(l, node, n):
    visit = [False for _ in range(n)]
    d = deque()
    d.append(node)
    visit[node-1] = True

    while d:
        new_node = d.popleft()
        print(new_node, end=" ")
        tl = l[new_node-1]
        for i in range(n):
            if not visit[i] and tl[i] == 1:
                d.append(i+1)
                visit[i] = True

    print()


if __name__ == "__main__":
    n, m, v = map(int, input().split())
    l = [[2 for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        x, y = map(int, input().split())
        l[x-1][y-1], l[y-1][x-1] = 1, 1

    d_visit = [False for _ in range(n)]

    DFS(l, v, n, d_visit)
    print()
    BFS(l, v, n)
