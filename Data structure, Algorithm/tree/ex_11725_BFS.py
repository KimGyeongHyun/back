from sys import stdin
from collections import deque

# 직접 트리를 구성해서 순회하면 시간복잡도가 올라감
# BFS 로 간단하게 도출 가능


if __name__ == "__main__":
    n = int(stdin.readline())
    g = [[] for _ in range(n+1)]
    for _ in range(n-1):
        f, s = map(int, stdin.readline().split())
        g[f].append(s)
        g[s].append(f)

    visit = [False for _ in range(n+1)]
    l = [0 for _ in range(n+1)]

    d = deque()
    d.append((1, 0))

    while d:

        child, parent = d.popleft()

        if l[child] != 0:
            continue

        l[child] = parent

        for num in g[child]:
            d.append((num, child))

    for num in l[2:]:
        print(num)
