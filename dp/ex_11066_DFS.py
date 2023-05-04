from sys import stdin
INF = int(1e9)

dp = []
l = []
presum = []

# 0) 문제 풀이

# 파일의 크기와 해당 파일 구성의 최소시간은 같은 값이 아니다
# 두 파일을 합칠 때 최소시간 = 두 파일의 크기 + 각각 두 파일 구성의 최소시간

# dp 구성 : dp[시작 인덱스][끝 인덱스]
# 시작 ~ 끝 의 파일 구성의 최소시간을 dp 에 저장한다

# 1) DFS (divide and conquer) - 시간초과
# 2) presum 사용 - 너무 긴 런타임
# 3) divide and conquer 방식 대신 dp 구성 순서를 직접 구성
# divide and conquer 방식을 사용할 경우 dp 에서 같은 값을 여러 번 부른다
# 대신 dp의 구성 순서를 알고 있다면 같은 값을 여러번 부르지 않아도 된다


def set_dp(k):
    """dp 구성"""

    # dp 구성 순서
    # 1~2, 2~3, 3~4 ...
    # 1~3, 2~4, 3~5 ...
    # ...
    # 1~k

    for gap in range(1, k):                   # 인덱스 간 격차
        for start in range(1, k+1-gap):         # 시작 인덱스

            min = INF
            midsum = presum[start+gap] - presum[start-1]

            for mid in range(start, start+gap):   # 중간 인덱스
                temp = midsum + dp[start][mid] + dp[mid+1][start+gap]
                if min > temp:
                    min = temp

            dp[start][start+gap] = min


if __name__ == "__main__":
    t = int(stdin.readline())
    for _ in range(t):
        k = int(stdin.readline())
        l = list(map(int, stdin.readline().split()))

        presum.clear()
        presum.append(0)
        for i in range(k):
            presum.append(presum[i] + l[i])

        dp = [[0 for _ in range(k+1)] for _ in range(k+1)]

        set_dp(k)
        print(dp[1][k])
