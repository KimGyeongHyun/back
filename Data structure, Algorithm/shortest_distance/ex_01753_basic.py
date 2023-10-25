import sys
input = sys.stdin.readline
INF = int(1e9)

# 다익스트라 알고리즘
# 1) 간선의 최대 거리가 10이라 하더라도, 최단거리는 10 을 넘어갈 수 있다

def get_smallest_index(d, v, visit):
    min_value = INF
    index = 0
    for i in range(1, v+1):
        if not visit[i] and d[i] < min_value:
            min_value = d[i]
            index = i

    return index


def dijkstra(g, v, start):
    visit = [False for _ in range(v + 1)]
    distance = [INF for _ in range(v + 1)]

    for end, dist in g[start]:
        if dist < distance[end]:
            distance[end] = dist

    distance[start] = 0
    visit[start] = True

    for _ in range(v-1):

        index = get_smallest_index(distance, v, visit)
        visit[index] = True

        for end, dist in g[index]:
            middle_dist = distance[index] + dist
            if middle_dist < distance[end]:
                distance[end] = middle_dist

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
