import math

# 해당 풀이는 재귀 없이 dp를 채우는 방식 사용
# 풀이가 6배 정도 빠름
# divide and conquer 방식은 똑같은 값을 계속 불러옴
# 해당 풀이는 dp 구성 순서를 직접 만듦


def solve():
    n = int(input())
    arr = [int(x) for x in input().split()]
    rst = [[0 for _ in range(n)] for _ in range(n)]

    for j in range(1, n):
        for i in range(j-1, -1, -1):
            small = math.inf

            for k in range(j-i):
                small = min(small, rst[i][i+k] + rst[i+k+1][j])
            rst[i][j] = small + sum(arr[i:j+1])
    print(rst[0][n-1])


t = int(input())
for _ in range(t):
    solve()