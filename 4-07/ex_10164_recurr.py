d = [[0] * 20 for _ in range(20)]


def dp(r, c):

    # r, c 까지 가는 경로 수를 재귀적 호출
    # r, c 에 대해 다이나믹 프로그래밍
    # 거리 차이가 1 이면 1 리턴
    # 해당 r, c 를 알고 있으면 그대로 리턴
    # 없으면 재귀 호출

    # 거리 차이가 1이라면 1을 리턴
    if r == 0 or c == 0:
        return 1
    # 이미 해당 경로 수를 알고 있으면 그대로 리턴
    if d[r][c] > 0:
        return d[r][c]

    # r, c 경로 수 모르면 재귀 호출
    # 해당 경로 수를 구해 다이나믹 프로그래밍 수행
    d[r][c] = dp(r-1, c) + dp(r, c-1)
    return d[r][c]


if __name__ == "__main__":
    n, m, k = map(int, input().split())

    # 경우지점 없음
    if k == 0:
        print(dp(n-1, m-1))

    else:
        r1, c1 = (k-1)//m, (k-1)%m
        r2, c2 = n-r1-1, m-c1-1
        print(dp(r1, c1) * dp(r2, c2))
