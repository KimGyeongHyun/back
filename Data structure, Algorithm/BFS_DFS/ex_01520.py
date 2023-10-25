from sys import stdin
xy_case = 0

# 1) visit 없는 DFS
# 시간 초과 발생

# 2) DFS 에서 끝까지 간 곳을 True 처리한 visit 만들어서 실행
# 시간, 메모리 초과 발생
# 또한 중복된 경로를 포함하지 못함

# 3) graph 구성
# 최대 250,000 개의 노드 존재
# 그래프를 배열로 구성하지 말고 append 로 구성해야 함
# 하지만 그래프 생성의 이점이 없음

# 4) 특정 (x, y) 지점에서 도착 지점까지 dp 로 저장
# 또한 해당 점이 출발 점의 숫자보다 크다면 예외 처리
# 문제가 풀리긴 했지만 다른 풀이에 비해 30배 가량 느림


def get_xy_way(n, m, x, y, l, dp):

    global xy_case

    if dp[y][x][1] is True:
        # print("second catch!")
        xy_case += dp[y][x][0]
        return

    if x == m-1 and y == n-1:
        xy_case += 1
        return

    if x >= 1 and l[y][x] > l[y][x-1]:
        get_xy_way(n, m, x-1, y, l, dp)
    if x <= m-2 and l[y][x] > l[y][x+1]:
        get_xy_way(n, m, x+1, y, l, dp)
    if y >= 1 and l[y][x] > l[y-1][x]:
        get_xy_way(n, m, x, y-1, l, dp)
    if y <= n-2 and l[y][x] > l[y+1][x]:
        get_xy_way(n, m, x, y+1, l, dp)


def get_all_way(n, m, l, dp):
    global xy_case

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):

            if l[i][j] >= l[0][0] and i != 0 and j != 0:
                # print("first catch!")
                dp[i][j] = (0, True)
                continue

            xy_case = 0
            get_xy_way(n, m, j, i, l, dp)
            dp[i][j] = (xy_case, True)

            # for k in range(n):
            #     for p in range(m):
            #         print(dp[k][p][0], end=' ')
            #     print()
            # print()


if __name__ == "__main__":
    n, m = map(int, stdin.readline().split())
    l = []
    for _ in range(n):
        l.append(list(map(int, stdin.readline().split())))

    dp = [[(0, False) for _ in range(m)] for _ in range(n)]

    get_all_way(n, m, l, dp)
    print(dp[0][0][0])
