
from sys import stdin

MONTH_DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
DAYS_SUM = 365
flowers = []


def get_days_from_0(month, day):

    days = day
    for i in range(1, month):
        days += MONTH_DAYS[i]

    return days


def get_flowers():

    p_start = get_days_from_0(3, 1)     # 3월 1일
    start = get_days_from_0(3, 1)       # 꽃이 피기 시작해야 하는 시작 날짜
    p_end = get_days_from_0(11, 30)     # 11월 30일
    end = -1                            # 꽃이 최대한 유지되는 마지막 날짜
    count = 0                           # 꽃의 갯수

    # 꽃이 1개일 경우 예외처리
    if len(flowers) == 1:
        if flowers[0][0] <= p_start and p_end < flowers[0][1]:
            return 1
        else:
            return 0

    for i in range(len(flowers)):
        s, e = flowers[i]   # s: 꽃 부화, e: 꽃 짐
        # print(i, s, e, start, end, count)

        # 꽃이 피기 시작해야 하는 날자를 지나 꽃이 피기 시작하면 예외처리
        if start < s:
            return 0

        # 하나의 꽃이 3/1 ~ 11/30 을 모두 포함하면 예외처리
        if s <= p_start and p_end < e:
            return 1

        if i == len(flowers)-1:
            if e <= p_end and end <= p_end:
                return 0

            if s <= p_end < e or s <= p_end < end:
                return count+1

        # 다음 꽃의 꽃 부화, 지는 날짜
        s2, e2 = flowers[i+1]

        # 꽃이 지는 날짜가 11월 30일을 포함하면 해당 꽃까지 포함시키고 리턴
        if e > p_end:
            return count+1

        # e <= start 일 경우는 end 값을 갱신할 일이 없지만
        # 다음 꽃이 start 를 넘는 조건을 확인해야 하므로
        # end = max(end, e) 로 퉁친다
        if s <= start < e:
            end = max(end, e)
            if start < s2:
                count += 1
                start = end


if __name__ == "__main__":
    n = int(stdin.readline())

    for _ in range(n):
        ff, fs, sf, ss = map(int, stdin.readline().split())
        flowers.append((get_days_from_0(ff, fs), get_days_from_0(sf, ss)))

    flowers.sort(key=lambda x: (x[0], x[1]))

    print(get_flowers())

