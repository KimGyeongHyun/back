import sys
input = sys.stdin.readline


# 문제 : 배열을 나눠 모든 (최댓값 - 최솟값) 중 최댓값이 최솟값이 나오는 것을 찾음
# 해당 최솟값을 이분 탐색으로 찾을 예정

# mid : 임의의 최솟값, count : mid 를 기준으로 나오는 배열의 최소 갯수
# m : 나와야 하는 나뉜 배열의 갯수
# 1. mid 와 count 는 반비례
# 2. m = count 조건일 때에도 mid 의 최솟값을 계속 찾아야 함
# (m >= count 조건일 때 max 값을 계속 갱신하여
#   m >= count 조건을 만족하며 count 를 극한까지 높히는 방향으로 다가가기)

# 말 그대로 mid 일 때 나뉜 배열의 최소 갯수인 count 를 구하는 것이기 때문에
# 실제로 count 보다 더 많이 배열이 나뉠 수 있음
# 하지만 문제에선 m개의 제한된 배열로 최댓값을 구하는 것이기 때문에
# 불필요하게 배열을 나누지 않음

# mid 에서 배열을 최소로 나눠 count 를 도출한 것이,
# count 개의 나뉜 배열에서 모든 (최댓값 - 최솟값) 중 최댓값이 최솟값이 mid 가 나온다는 증명이 필요

# 1. count 개의 나뉜 배열에서 mid 를 도출할 수 있다
# 2. mid 보다 작은 값을 count 로 도출할 수 있는지 증명 필요
# 그전에 만약 증명이 필요 없이 mid 보다 작은 값으로도 도출이 가능할 때
# 이분 탐색으로 자연스럽게 예외 처리되는지 확인해야 함

# 극한까지 mid 를 탐색하여 (mid -> m, mid-1 -> m이상) 의 결과를 찾았다고 가정
# m 개에선 mid이하까지 도출 가능, m 초과 개에선 mid-1 이하까지 도출 가능


# 1 5 3 8 20 21 / mid = 5 인 경우
# 1, 5, 3 으로 자르면 8, 20 사이에 갭이 생겨 구성이 불가능하다고 판단이 된다
# 하지만 1, 5 / 3, 8 로 나누면 구성이 가능하다
# 즉 앞쪽에서 쭉 봤을 때도 값이 넘는지 확인하는 것이 중요하지만
# 뒤쪽에서 보는 것도 생각해야 한다

# 만약 앞쪽에서 비교하다가 mid 를 넘는 값이 발견 되었다면
# 해당 인덱스의 앞쪽 수를 참고할 수 있는지 여부 확인 필요
# 만약 앞쪽 수에 포함할 수 있는 수가 없으면 인덱스를 넘기면 된다

# 앞쪽 수는 하나만 확인하면 된다
# 되면 되는 거고 안 되면 안 되는 것

if __name__ == "__main__":
    n, m = map(int, input().split())
    l = list(map(int, input().split()))

    start = 1
    end = 5000 * 10000
    result = 0

    while start <= end:
        mid = (start + end) // 2
        min = 1
        max = 10000
        index = 0
        count = 0
        over_two = 0
        impossible_flag = False

        while index <= n-2:
            print("index :", index)
            f, s = l[index], l[index+1]
            if f <= s:
                min = f
                max = s
            else:
                min = s
                max = f

            if max - min > mid:
                if over_two == 0:
                    impossible_flag = True
                    break

                over_two = 0
                if -mid < l[index-1] - l[index] < mid:
                    count += 1
                    index += 1
                    continue
                else:
                    impossible_flag = True
                    break

            count += 1
            index += 2
            over_two = 0

            while index <= n-1:
                t = l[index]
                index += 1
                over_two += 1
                if t < min:
                    min = t
                if max < t:
                    max = t
                if max - min > mid:
                    break

        print(start, mid, end, count, result)

        if m >= count and not impossible_flag:
            result = mid
            end = mid - 1
        else:
            start = mid + 1

    print(result)