from sys import stdin

MONTH_DAYS = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]    # 월 당 일수
flowers = []    # 꽃들 [꽃 인덱스](꽃이 피는 날짜, 꽃이 지는 날짜)    (꽃이 피는 날짜 기준 정렬)

# 작동 방식
# 꽃들이 꽃이 피는 날짜로 정렬되어 있다는 전제 하
# 꽃이 피기 시작해야 하는 날짜를 지정한다 (start)
# (처음 start 는 3월 1일)
# 해당 날짜까지 꽃이 피기 시작하는 꽃들을 모은다
# (start 가 3월 1일이라면 꽃이 피기 시작하는 날짜가 1월 1일 ~ 3월 1일 에 있는 꽃들)
# 모은 꽃들 중 꽃이 지는 날짜 중 제일 큰 날짜를 찾는다 (end)
# 그러면 최대 start ~ end 일까지 하나의 꽃이 피어있다고 볼 수 있다
# 즉, 다음으로 꽃이 피기 시작해야 하는 날짜(start)를 end 로 갱신하고, 총 꽃의 숫자(count)를 +1 한다
# 갱신된 start 값으로 위의 과정을 반복한다 (line 11 ~ 15)

# 예외사항
# 1) 꽃이 피기 시작해야 하는 날짜(start)부터 꽃들을 모을 때 꽃이 하나도 없다면
# 중간에 공백기가 있다는 의미이므로 0을 리턴한다
# 2) 모은 꽃들 중 꽃이 지는 날짜 중 제일 큰 날짜(end)를 찾는중 11월 30일이 넘어갔다면
# 해당 꽃을 마지막으로 3월1일 ~ 11월30일의 영역에서 꽃이 핀다는 의미이므로
# 총 꽃의 숫자(count) + 1 을 리턴한다
# 3) 마지막 꽃이라면
# end 가 11월 30일을 넘지 못한다면 11월 30일까지 꽃이 피지 못한다는 의미이므로
# 0을 리턴한다
# 11월 30일을 넘었다면 예외사항 2)랑 똑같이 count+1 을 리턴한다


def get_days_from_0(month, day):
    """월/일 을 받고 총 일수를 리턴하는 메소드"""

    days = day
    for i in range(1, month):
        days += MONTH_DAYS[i]

    return days


def get_flowers():
    """꽃이 피기 시작하는 날짜로 정렬된 꽃들 중 3월1일 ~ 11월30일 내에 항상 꽃이\n
    피어 있고, 그때 꽃의 최소 갯수를 리턴하는 메소드"""

    p_end = get_days_from_0(11, 30)     # 11월 30일
    start = get_days_from_0(3, 1)       # 꽃이 피기 시작해야 하는 시작 날짜
    end = -1                            # start 에서부터 꽃이 최대로 유지되는 마지막 날짜
    count = 0                           # 꽃의 갯수

    for i in range(len(flowers)):
        s, e = flowers[i]   # s: 꽃 부화, e: 꽃 짐

        # 1)
        if start < s:
            return 0

        # 제일 큰 end 찾음
        end = max(e, end)

        # 3)
        if i == len(flowers)-1:
            if end <= p_end:
                return 0
            else:
                return count+1

        # 다음 꽃의 꽃 부화, 지는 날짜
        s2, e2 = flowers[i+1]

        # 2)
        if end > p_end:
            return count+1

        # 현재 꽃이 피는 날이 start 를 넘지 않고
        # 다음 꽃이 피는 날이 start 를 넘으면
        # 현재 꽃까지 1개로 본다
        # start 를 end 로 갱신, count += 1
        if s <= start < s2:
            count += 1
            start = end


if __name__ == "__main__":
    n = int(stdin.readline())

    for _ in range(n):
        ff, fs, sf, ss = map(int, stdin.readline().split())
        flowers.append((get_days_from_0(ff, fs), get_days_from_0(sf, ss)))

    # 2차원 정렬
    flowers.sort(key=lambda x: (x[0], x[1]))

    print(get_flowers())

