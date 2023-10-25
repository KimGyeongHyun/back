from sys import stdin
from collections import deque

# 노드 갯수가 많으므로 트리를 직접 구성하면 시간 초과가 발생
# 그래프의 방향성이 없으므로 어느 방향이 루트 방향인지를 알아야 함

# LCA 알고리즘
# 최소 공통 조상을 구하는 알고리즘
# (부모 노드, 깊이) 배열 구성
# 두 노드 비교할 때 먼저 깊이를 맞추고 노드가 같아질 때까지 부모 노드로 올라감

# 위의 알고리즘만 적용할 때 극단적인 상황에선 시간 초과 발생 (PyPy3 에선 통과)
# (왼쪽, 오른쪽 1만개 길이의 노드의 최소 공통 조상을 5만번 찾음)

# dp 를 사용하여 풀었지만 시간 복잡도상 좋지 않음 (편법 풀이)


def get_near_parent(input_a, input_b):
    """가장 가까운 공통 조상 리턴"""

    a, b = input_a, input_b
    # print("first ", a, b)

    while True:

        depth1, depth2 = par[a][1], par[b][1]
        # print(a, b, depth1, depth2)

        if depth1 < depth2:
            b = par[b][0]
            continue

        if depth1 > depth2:
            a = par[a][0]
            continue

        if a != b:
            a = par[a][0]
            b = par[b][0]
            continue

        return a


if __name__ == "__main__":
    n = int(stdin.readline())
    g = [[] for _ in range(n+1)]
    visit = [False for _ in range(n+1)]
    par = [0 for _ in range(n+1)]
    for _ in range(n-1):
        d1, d2 = map(int, stdin.readline().split())
        g[d1].append(d2)
        g[d2].append(d1)

    d = deque()
    d.append((0, 1, 0))

    while d:
        parent, child, depth = d.popleft()

        if visit[child]:
            continue
        visit[child] = True

        par[child] = (parent, depth)

        for c_child in g[child]:
            d.append((child, c_child, depth+1))

    m = int(stdin.readline())
    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        print(get_near_parent(a, b))
