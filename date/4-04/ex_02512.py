from sys import stdin


def get_total_money(input_list, input_margin):
    """각 지방 예산요청 리스트, 상한선을 받아 총 예산을 리턴"""

    sum_money = 0
    for money in input_list:
        sum_money += min(money, input_margin)

    return sum_money


if __name__ == "__main__":
    n = int(stdin.readline())
    l = list(map(int, stdin.readline().split()))
    m = int(stdin.readline())

    # 이분법 도입
    start = 0
    end = max(l)

    while True:

        mid = (start + end) // 2

        # 탐색 범위가 2라면 탈출 (start + 1 = end)
        if start == mid:
            # end 에서 조건 만족할 경우 mid 를 end 로 바꿈
            # 아닐 경우 mid 를 start 그대로 유지
            if get_total_money(l, mid + 1) <= m:
                mid += 1
            break

        sum_money = get_total_money(l, mid)

        # sum_money == m 일 경우에도 바로 while 문을 탈출하지 않고
        # 혹시 모를 더 큰 mid 값이 있는지 탐색한다
        if sum_money <= m:
            start = mid
        else:
            end = mid

    print(mid)
