import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

# 다익스트라 알고리즘
# 최소 힙 자료구조 사용
# study_algorithm/shortest_distance 의 dijkstra_heap.py 를 참고함

def dijkstra(g, v, start):
    distance = [INF for _ in range(v + 1)]
    distance[start] = 0

    q = []
    heapq.heappush(q, (0, start))

    while q:

        i_dist, index = heapq.heappop(q)

        if distance[index] < i_dist:
            continue

        for end, dist in g[index]:
            mid_dist = distance[index] + dist
            if mid_dist < distance[end]:
                distance[end] = mid_dist
                heapq.heappush(q, (mid_dist, end))

    for number in distance[1:]:
        if number == 1000000000:
            print("INF")
        else:
            print(number)


if __name__ == "__main__":
    V, E = map(int, input().split())
    g = [[] for _ in range(V+1)]

    start = int(input())
    for _ in range(E):
        s, e, d = map(int, input().split())
        g[s].append((e, d))

    dijkstra(g, V, start)

