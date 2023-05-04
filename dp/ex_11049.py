from sys import stdin
input = stdin.readline
INF = int(1e9)
dp = []
l = [(0, 0)]


def set_dp(n):

    for gap in range(2, n+1):
        for i in range(1, n-gap+2):

            min = INF

            for mid in range(i, i+gap-1):
                temp = dp[i][mid] + dp[mid+1][i+gap-1]
                temp += l[i][0] * l[mid][1] * l[i+gap-1][1]

                if temp < min:
                    min = temp

            dp[i][i+gap-1] = min


if __name__ == "__main__":
    n = int(input())

    for _ in range(n):
        l.append(tuple(map(int, input().split())))

    l.append((0, 0))

    dp = [[0 for _ in range(n+2)] for _ in range(n+2)]
    set_dp(n)

    print(dp[1][n])