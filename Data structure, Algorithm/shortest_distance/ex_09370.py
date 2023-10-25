from sys import stdin
import heapq
INF = int(1e9)


# 다익스트라 배열을 리턴
def dijkstra(g, n, s):

    distance = [INF for _ in range(n+1)]
    distance[s] = 0

    q = []
    heapq.heappush(q, (0, s))

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

    T = int(stdin.readline())

    for _ in range(T):
        n, m, t = map(int, stdin.readline().split())
        gr = [[] for _ in range(n+1)]   # 그래프
        way = []    # 마지막 도착지들

        s, g, h = map(int, stdin.readline().split())

        # 그래프 구성
        for _ in range(m):
            a, b, d = map(int, stdin.readline().split())
            gr[a].append((b, d))
            gr[b].append((a, d))

        # 마지막 도착지 구성
        for _ in range(t):
            way.append(int(stdin.readline()))

        # 출발 지점의 최단경로 배열
        sd = dijkstra(gr, n, s)

        # 도착지까지 가는데 g와 h를 무조건 거쳐야 한다
        # 이때 도착 지점까지 최단경로로 간다고 보장하므로 g, h 중 출발지에서 가까운 점을 먼저 간 다음에 다른 점으로 거쳐 간다고 볼 수 있다
        # 예를 들어 g보다 h가 출발점으로부터 더 가깝다면
        # 출발점 -> h -> g -> 도착지점
        # 의 순서로 이동할 것이다
        # mid : 거처가는 두 지점 중 출발점으로부터 더 먼 지점
        if sd[g] < sd[h]:
            mid = h
        else:
            mid = g

        # mid 점에서 다시 최단경로 배열을 구한다
        md = dijkstra(gr, n, mid)

        # 도착 지점을 추려서 저장
        index = []

        # 출발 -> 도착 경로가 최단경로라면
        # "출발 -> mid -> 도착" 경로는 "출발 -> 도착"과 같아야 한다
        # 해당 조건을 만족하는 도착 지점을 저장하여 출력한다
        for node in way:
            if sd[mid] + md[node] == sd[node]:
                index.append(node)

        index.sort()
        print(*index)