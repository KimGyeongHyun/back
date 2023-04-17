from sys import stdin
import heapq
INF = int(1e9)


def dijkstra(g, n, start):
    distance = [INF for _ in range(n+1)]
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))

    while q:

        i_dist, index = heapq.heappop(q)

        if distance[index] < i_dist:
            continue

        for end, dist in g[index]:
            mid_dist = i_dist + dist
            if mid_dist < distance[end]:
                distance[end] = mid_dist
                heapq.heappush(q, (mid_dist, end))

    return distance


if __name__ == "__main__":
    N, E = map(int, stdin.readline().split())
    g = [[] for _ in range(N+1)]
    for _ in range(E):
        a, b, c = map(int, stdin.readline().split())
        g[a].append((b, c))
        g[b].append((a, c))
    v1, v2 = map(int, stdin.readline().split())
    sd = dijkstra(g, N, 1)
    v1d = dijkstra(g, N, v1)
    v2d = dijkstra(g, N, v2)

    v12 = sd[v1] + v1d[v2] + v2d[N]
    v21 = sd[v2] + v2d[v1] + v1d[N]

    if v12 < v21:
        min_dist = v12
    else:
        min_dist = v21

    if min_dist >= 1000000000:
        print(-1)
    else:
        print(min_dist)