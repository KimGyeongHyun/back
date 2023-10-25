import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

l = []
dp = []

# 1520 문제와 같이 divide and conquer 방식 사용


def get_big_dist(n, x, y):

    # print(x, y)
    # print_dp()

    if dp[y][x] != -1:
        return dp[y][x]

    ways = 1
    if x >= 1 and l[y][x] < l[y][x-1]:
        ways = max(ways, get_big_dist(n, x-1, y) + 1)
    if x <= n-2 and l[y][x] < l[y][x+1]:
        ways = max(ways, get_big_dist(n, x+1, y) + 1)
    if y >= 1 and l[y][x] < l[y-1][x]:
        ways = max(ways, get_big_dist(n, x, y-1) + 1)
    if y <= n-2 and l[y][x] < l[y+1][x]:
        ways = max(ways, get_big_dist(n, x, y+1) + 1)

    dp[y][x] = ways
    return ways


def print_dp():
    for line in dp:
        print(*line)
    print()


if __name__ == "__main__":
    n = int(input())
    for _ in range(n):
        l.append(list(map(int, input().split())))

    dp = [[-1 for _ in range(n)] for _ in range(n)]

    big = 0
    for i in range(n):
        for j in range(n):
            big = max(big, get_big_dist(n, i, j))

    print(big)