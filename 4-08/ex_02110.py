import sys
input = sys.stdin.readline

# 문제 조건 : 주어진 c개의 점에서 각 점 간의 거리의 최솟값이 최댓값이 되는 조건을 찾아야 함
# 해당 최댓값을 이분 탐색으로 찾을 예정

# mid : 특정 거리 최댓값, count : mid 기준으로 나오는 점의 최대 갯수
# c : 나와야 하는 점의 갯수
# mid(거리) 가 주어졌을 때 역으로 c를 찾아야 함
# 1. mid 와 count는 반비례
# 2. c = count 조건일 때에도 mid 의 최댓값을 계속 찾아야 함
# (c <= count 조건일 때 min 값을 계속 갱신하여
#   c <= count 조건을 만족하며 count 를 극한까지 낮추는 방향으로 다가가기)

# 임의의 mid 에 대하여 실측 공유기 간 거리의 최솟값은 다를 수 있다
# 하지만 이분 탐색을 모두 돌아 갱신이 된 mid 값은 실측 최솟값과 같다

# 증명
# c <= count 일 때까지 mid 를 올리고,
# c > count 이면 다시 mid 를 내리는 식으로 반복
# 끝까지 반복한다면, c <= count 를 만족하는 최댓값 mid 가 갱신 되어 있을 것
# 즉, mid+1 은 c > count 의 조건으로 들어감


if __name__ == "__main__":
    n, c = map(int, input().split())
    l = []
    for _ in range(n):
        l.append(int(input()))

    l.sort()

    min = 1             # 최소값
    max = 1000000000    # 최대값
    result = 0          # 조건을 만족할 때마다 정답 갱신

    while min <= max:
        mid = (min + max) // 2

        count = 0   # mid 거리 기준 최대 공유기 갯수
        index = 0   # l 탐색 위한 인덱스

        # 집의 좌표를 쭉 돌며 mid 상황에서 count 를 찾음
        while index <= n - 1:

            start = l[index]  # 거리 비교를 시작할 공유기 위치
            count += 1  # 공유기가 배치되었으니 count + 1

            # mid 거리 미만까지 index + 1
            while True:
                index += 1
                if index >= n:
                    break
                # 탈출 조건
                # 간 거리가 mid 이상
                if l[index] - start > mid - 1:
                    break

        # 이분 탐색
        if c <= count:
            result = mid    # 정답 갱신
            min = mid + 1
        else:
            max = mid - 1

    print(result)
