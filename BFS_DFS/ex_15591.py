from sys import stdin
from collections import deque

# 플로이드 알고리즘으로 모든 동영상 간의 USADO를 구하기엔 동영상의 갯수가 너무 많다
# 우선 n-1 개의 간선을 어떻게 받고 처리할 것인지 생각해야 한다

# 1)
# key : 출발 동영상, value : (도착 동영상, 두 동영상의 USADO)
# 두 동영산 간의 USADO 를 구하는 메소드 생성
# 해당 메소드로 정답을 구하려고 하면 시간 초과 발생

# 2)
# 직접 동영상의 갯수를 리턴하는 메소드가 필요
# k 이상의 조건에서 USADO 를 구하면서 계속 카운트를 늘린다
# USADO 가 k보다 작은 값으로 갱신이 되면 탈출하고 카운트를 리턴한다


# def get_USADO(g, n, f, s):
#
#     visit = [False for _ in range(n+1)]
#
#     d = deque()
#     d.append((f, 1000000000))
#
#     while d:
#         app, u = d.popleft()
#
#         if visit[app] is True:
#             continue
#
#         if app == s:
#             return u
#
#         visit[app] = True
#
#         for l, lu in g[app]:
#             d.append((l, min(u, lu)))


def get_video_number(g, n, s, k):

    visit = [False for _ in range(n+1)]

    d = deque()
    d.append((s, 1000000000))
    count = -1

    while d:
        e, u = d.popleft()

        if visit[e]:
            continue

        if u >= k:
            count += 1
        else:
            continue

        visit[e] = True

        for l, ul in g[e]:
            d.append((l, ul))

    return count


if __name__ == "__main__":
    N, Q = map(int, stdin.readline().split())
    g = [[] for _ in range(N+1)]

    for _ in range(N-1):
        p, q, r = map(int, stdin.readline().split())
        g[p].append((q, r))
        g[q].append((p, r))

    for _ in range(Q):
        k, v = map(int, stdin.readline().split())

        print(get_video_number(g, N, v, k))

