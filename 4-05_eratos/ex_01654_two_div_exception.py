from sys import stdin

# 1) 이분법 알고리즘 미적용으로 시관초과 발생
# 이분법 알고리즘 도입
# 2) get_wire_count(mid), get_wire_count(mid+1) 차이가 1이 나는 곳만 정답으로 유추
# get_wire_count 는 상황에 따라 +2 이상의 차이가 날 수 있음
# 조건을 get_wire_count(mid) > get_wire_count(mid+1) 로 수정
# 3) 이분법 적용 중 start_wire_range = mid 일 경우 end_wire_range 를 탐색하지 않고
#   무한 루프에 빠지는 문제 발생
# start_wire_range = mid 의 경우 mid, mid+1 둘 다 탐색하게 수정
# 4) get_wire_count(mid) = n 을 굳이 만족할 필요 없이
#   get_wire_count(mid) >= n 이어도 된다는 것을 인지 못함
#   물론 get_wire_count(mid) = n 의 조건이 없을 때까지 mid 를 찾아야함
# get_wire_count(mid) = n 일 때까지 mid 를 끝까지 탐색하다가
# 위의 조건을 만족하지 않으면 get_wire_count(mid) > n 의 조건 추가
# 5) ZeroDivisionError 발생
# 해당 문제는 0 ~ 3 탐색 중 mid = 1을 비교하는 도중
# get_wire_count(mid) = n 을 만족하지 않아 (실제로 mid = 1일 경우가 정답임)
# mid = 0 으로 보내버리기 때문에 발생한다
# mid = 0 일 경우 mid = 1 로 출력하도록 수정
# 6) 예외처리에만 집중하여 전반적인 알고리즘이 지저분함
# 5번 문제의 경우 mid+1 을 먼저 비교하여 mid = 0 을 가기 전에 예외처리 하도록 변경

wire_list = []


def get_wire_count(wire_range):

    count = 0
    for wire in wire_list:
        count += wire // wire_range

    return count


if __name__ == "__main__":

    k, n = map(int, stdin.readline().split())

    for _ in range(k):
        wire_list.append(int(stdin.readline()))

    # 1)
    start_wire_range = 0
    end_wire_range = max(wire_list)

    while True:

        mid = (start_wire_range + end_wire_range) // 2

        # 3)
        if start_wire_range == mid:
            # 6)
            upcount = get_wire_count(mid+1)
            # 2), 4), 5)
            if upcount >= n and upcount > get_wire_count(mid + 2):
                mid += 1
            break

        count = get_wire_count(mid)

        if count < n:
            end_wire_range = mid
        else:
            start_wire_range = mid

    print(mid)
