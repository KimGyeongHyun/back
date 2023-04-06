import sys
input = sys.stdin.readline

# 문제 조건 : m개의 나뉜 배열의 각 총합이 최소가 되는 값을 찾아야 함
# 해당 최솟값을 이분 탐색으로 찾을 예정

# mid : 특정 최솟값, count : mid 를 기준으로 나오는 나뉜 배열 갯수
# 1. mid 와 count 는 반비례
# 2. m = count 조건일 대에도 mid 의 최솟값을 계속 찾아야 함
# (m >= count 조건을 만족하며 count 가 변화가 없을 때까지 max 값을 계속 갱신하며 mid 값을 최소로 구함)

if __name__ == "__main__":
    n, m = map(int, input().split())
    l = list(map(int, input().split()))

    min = max(l)    # 블루레이 최소 재생시간은 모든 강의 길이보단 크거나 같아야 한다
    max = 10000 * 100000    # 강의 최대 재생시간 * 강의 최대 개수
    result = 0      # 정답 갱신

    # 이분 탐색
    while min <= max:
        mid = (min + max) // 2

        count = 0   # 나뉜 배열 개수
        index = 0   # 배열 탐색 인덱스
        # 배열 나누기
        while index <= n - 1:
            # 배열 추가
            sum = l[index]
            count += 1

            # 배열 총합이 mid 를 넘지 않을 때까지 index + 1
            while True:
                index += 1
                # 남아있는 수가 없으면 탈출
                if index >= n:
                    break

                # 배열에 새로 추가된 수를 배열 총합에 더함
                sum += l[index]
                # 총합이 mid 를 넘으면 탈출
                if mid < sum:
                    break

        if m < count:
            min = mid + 1
        else:
            result = mid
            max = mid - 1

    print(result)
