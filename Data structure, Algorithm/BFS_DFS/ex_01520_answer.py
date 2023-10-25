import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline
dp = []
l = []

# 모든 점의 경로의 수를 구하는 게 아닌 divide and conquer 방식으로 필요한 점의 경로의 수만 구한다
# dp를 구할 때 divide and conquer 방식이 유용할 수 있음을 생각하자


def dfs(n, m, x, y):

    if x == m-1 and y == n-1:
        return 1

    if dp[y][x] != -1:
        return dp[y][x]

    ways = 0

    if 1 <= x and l[y][x] > l[y][x-1]:
        ways += dfs(n, m, x-1, y)
    if x <= m-2 and l[y][x] > l[y][x+1]:
        ways += dfs(n, m, x+1, y)
    if 1 <= y and l[y][x] > l[y-1][x]:
        ways += dfs(n, m, x, y-1)
    if y <= n-2 and l[y][x] > l[y+1][x]:
        ways += dfs(n, m, x, y+1)

    dp[y][x] = ways
    return ways


if __name__ == "__main__":
    n, m = map(int, input().split())
    for _ in range(n):
        l.append(list(map(int, input().split())))

    dp = [[-1 for _ in range(m)] for _ in range(n)]

    print(dfs(n, m, 0, 0))