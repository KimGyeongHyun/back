import sys
input = sys.stdin.readline

# 문제 : 배열을 나눠 모든 (최댓값 - 최솟값) 중 최댓값이 최솟값이 나오는 것을 찾음
# 해당 최솟값을 이분 탐색으로 찾을 예정

# mid : 임의의 최솟값, count : mid 를 기준으로 나오는 배열의 최대 갯수
# m : 나와야 하는 나뉜 배열의 갯수
# 1. mid 와 count 는 반비례
# 2. m = count 조건일 때에도 mid 의 최댓값을 계속 찾아야 함
# (m <= count 조건일 때 min 값을 계속 갱신하여
#   m <= count 조건을 만족하며 count 를 극한까지 낮추는 방향으로 다가가기)

if __name__ == "__main__":
    n, m = map(int, input().split())
    l = list(map(int, input().split()))

    min = 1
    max = 5000 * 10000

    while min <= max:
        mid = (min + max) // 2

        start = l[index]