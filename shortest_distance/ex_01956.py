from sys import stdin
from collections import deque
INF = int(1e9)

# 그래프 특정 노드에서 최소 사이클을 구하는 문제

# 1)
# 1번 노드에서 BFS 탐색
# 방문한 노드 처리를 어떻게 할 것인지 생각하기
# 다른 노드들은 정상적으로 방문 처리를 하고 1번 노드만 예외처리하면 된다
# 1번 노드에 도달했을 때 weight 가 작으면 갱신
# 벨만 포드처럼 노드갯수 - 1 개만큼 수행하면 된다
# 해당 문제는 모든 노드에 대한 최대경로를 구할 필요 없이 사이클을 모두 찾고 비교하면 된다
# visit 처리 어떻게 할지 자세히 생각해야 함

# visit 을 BFS 메소드 내부에 두게 되면 다른 경우의 수가 다른 노드로 갈 경우
# True 로 설정하기 때문에 해당 노드를 방문하지 않는다
# 3 4
# 1 2 1
# 2 3 1
# 3 1 1
# 2 1 3
# start with : 1
# end with: 3
# start with : 2
# end with: 4   <- 틀린 답
# start with : 3
# end with: 3
# 3
# 따라서 다른 방법을 사용해야 한다

# 2)
# 플로이드 워셜의 본인으로 가는 노드를 0으로 초기화하지 않고 그대로 진행한다
# 그러면 본인으로 도는 사이클 중 최단경로가 그래프에 저장될 것이다


def floyd(g, n):
    for mid in range(1, n+1):
        for start in range(1, n+1):
            for end in range(1, n+1):
                if g[start][mid] + g[mid][end] < g[start][end]:
                    g[start][end] = g[start][mid] + g[mid][end]


if __name__ == "__main__":
    v, e = map(int, stdin.readline().split())
    g = [[INF for _ in range(v+1)] for _ in range(v+1)]
    for _ in range(e):
        a, b, c = map(int, stdin.readline().split())
        g[a][b] = c

    # for line in g:
    #     print(line)

    floyd(g, v)

    # for line in g:
    #     print(line)

    min = INF
    for i in range(1, v+1):
        if g[i][i] < min:
            min = g[i][i]

    if min >= INF:
        print(-1)
    else:
        print(min)