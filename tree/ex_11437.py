from sys import stdin
from collections import deque

# 노드 갯수가 많으므로 트리를 직접 구성하면 시간 초과가 발생
# 그래프의 방향성이 없으므로 어느 방향이 루트 방향인지를 알아야 함


def get_near_parent(input_a, input_b):
    """가장 가까운 공통 조상 리턴"""

    al = []

    temp = input_a
    while True:
        al.append()


if __name__ == "__main__":
    n = int(stdin.readline())
    ig = [[] for _ in range(n+1)]
    for _ in range(n-1):
        d1, d2 = map(int, stdin.readline().split())
        ig[d1].append(d2)
        ig[d2].append(d1)

    g = [-1 for _ in range(n + 1)]
    d = deque()     # start, end
    d.append((0, 1))

    while d:

        start, end = d.popleft()

        if g[end] != -1:
            continue

        g[end] = start

        for num in ig[end]:
            d.append((end, num))

    m = int(stdin.readline())
    l = []
    for _ in range(m):
        a, b = map(int, stdin.readline().split())
        l.append(str(get_near_parent(a, b)))

    print("\n".join(l))
