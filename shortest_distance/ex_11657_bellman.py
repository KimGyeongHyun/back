from sys import stdin
INF = int(1e9)


def bellman_ford(edges, start, n, m):
    distance = [INF for _ in range(n+1)]
    distance[start] = 0
    for i in range(n):
        for j in range(m):
            s = edges[j][0]
            e = edges[j][1]
            r = edges[j][2]

            # 무한대 + 양수 간선은 갱신되어도 무한대보다 크기 때문에 상관 없지만
            # 무한대 + 음수 값이 갱신되면 해당 값은 더이상 무한대가 아님
            # 따라서 s 최단경로가 없을 때 갱신이 안 되게 함
            if distance[s] != INF and distance[s] + r < distance[e]:
                distance[e] = distance[s] + r

                if i == n-1:
                    print(-1)
                    return

    for i in range(2, n+1):
        l = distance[i]
        if l < INF:
            print(l)
        else:
            print(-1)


if __name__ == "__main__":

    n, m = map(int, stdin.readline().split())
    edges = []

    for _ in range(m):
        edges.append(tuple(map(int, stdin.readline().split())))
    bellman_ford(edges, 1, n, m)
