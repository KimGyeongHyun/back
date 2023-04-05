import sys
input = sys.stdin.readline


if __name__ == "__main__":
    n, m = map(int, input().split())
    l = list(map(int, input().split()))

    min = max(l)    # 블루레이 최소 재생시간은 모든 강의 길이보단 크거나 같아야 한다
    max = 10000 * 100000    # 강의 최대 재생시간 * 강의 최대 개수
    result = 0

    while min <= max:
        mid = (min + max) // 2

        count = 0
        index = 0
        while index <= n - 1:
            sum = 0

            # mid의 시간까지 강의시간을 넘긴다
            # index 를 mid 시간까지 계속 증가시킨다
            while sum + l[index] <= mid:
                sum += l[index]
                # print("sum, index :", sum, index)
                index += 1
                if index >= n:
                    break

            count += 1

        # print(" to min, mid, max, count :", min, mid, max, count)

        # mid 가 커지면 count 는 작아진다
        # result 는 m == count 를 만족하면서 mid 중 제일 큰 값일 때 갱신이 되어야 한다
        # mid 가 매우 큰 상태에서 count 가 m 보다 작을 때도 result 를 갱신한다
        # 그러다가 mid 가 적당히 커져 count <= m 을 만족하고,
        # mid+1의 경우 count > m 이 되는 경우까지 찾아야 한다

        if m < count:
            min = mid + 1
        else:
            result = mid
            max = mid - 1

        # print(" result :", result)

    print(result)