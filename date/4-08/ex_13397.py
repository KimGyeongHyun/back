import sys
input = sys.stdin.readline


# 문제 : 배열을 나눠 모든 (최댓값 - 최솟값) 중 최댓값이 최솟값이 나오는 것을 찾음
# 해당 최솟값을 이분 탐색으로 찾을 예정

# mid : 임의의 최솟값, count : mid 를 기준으로 나오는 배열의 최소 갯수
# m : 나와야 하는 나뉜 배열의 갯수
# 1. mid 와 count 는 반비례
# 2. m = count 조건일 때에도 mid 의 최솟값을 계속 찾아야 함
# (m >= count 조건을 만족하며 count 변화가 없을 때까지 max 값을 계속 갱신하여 mid 값을 줄인다)


# 이분 탐색을 통해 mid 를 끝까지 도출한 상태에서의 나뉜 배열의 갯수를 count 라고 한다면
# count 개의 나뉜 배열에서 모든 (최댓값 - 최솟값) 중 최댓값이 최솟값인 경우는 mid이다
# 라는 증명이 필요하다

# 증명
# 1. count 개의 나뉜 배열에서 mid 보다 작은 값들은 도출할 수 없다
#   mid -> count1, mid-1 -> count2 라고 했을 때
#   count1 > count2 가 성립한다  (mid 이분 탐색을 끝까지 했을 때)
# 2. count 개의 나뉜 배열에서 mid 를 도출할 수 있다
#   mid 에서 count 가 나온다는 것을 계산했다
# 3. count 개의 나뉜 배열에서 mid 보다 큰 값들도 도출할 수 있다
#   배열을 짧게 나눌수록 더욱 큰 값들도 나올 수 있다

# 극한까지 mid 를 탐색하여 (mid -> m, mid-1 -> m이상) 의 결과를 찾았다고 가정
# m 개에선 mid 이상까지 도출 가능, m 초과 개에선 mid-1 이상까지 도출 가능
# 즉, m 개의 나뉜 배열에선 mid 가 최대값


if __name__ == "__main__":
    n, m = map(int, input().split())
    l = list(map(int, input().split()))

    start = 0               # 시작점
    end = 5000 * 10000      # 끝점
    result = 0              # 정답 갱신

    # 이분 탐색
    while start <= end:
        mid = (start + end) // 2
        min = 1         # 나뉜 배열의 최솟값
        max = 10000     # 나뉜 배열의 최댓값
        index = 0       # 배열 순환 인덱스
        count = 0       # 나뉜 배열 갯수

        # 배열 갯수 계산
        while index <= n - 1:
            # 배열 추가
            count += 1
            index += 1
            # 남아있는 수가 없으면 탈출
            if index >= n:
                break

            # 배열 크기가 2가 되었다면
            # 배열 내 최댓값 최솟값 갱신
            f = l[index-1]
            s = l[index]
            if f < s:
                min = f
                max = s
            else:
                min = s
                max = f

            # 범위가 mid 보다 크다면 배열을 나눔
            if max - min > mid:
                continue

            # max - min <= mid 조건일 때까지 index + 1
            while True:
                index += 1
                # 남아있는 수가 없으면 탈출
                if index >= n:
                    break

                # min, max 값을 새로 들어온 수에 맞게 갱신
                t = l[index]
                if t < min:
                    min = t
                if max < t:
                    max = t

                # 범위가 mid 보다 크다면 배열을 나눔
                if max - min > mid:
                    break

        if m >= count:
            result = mid
            end = mid - 1
        else:
            start = mid + 1

    print(result)