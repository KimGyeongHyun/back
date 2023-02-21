def get_big_number(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= c:
        return b
    else:
        return c


if __name__ == "__main__":
    a, b, c = map(int, input().split())

    if a == b and a == c:
        print(a * 1_000 + 10_000)
    elif a == b or a == c:
        print(a * 100 + 1_000)
    elif b == c:
        print(b * 100 + 1_000)
    else:
        print(get_big_number(a, b, c) * 100)

    # if 한줄 표현으로 간결하게 해결
    # res = (a == b) + (b == c) + (c == a)
    # if res >= 2:
    #     print(10000 + a * 1000)
    # elif res == 1:
    #     # 더욱 짧고 간결한 표현
    #     v = b if a == b or b == c else a
    #     print(1000 + v * 100)
    # else:
    #     print(max(a, b, c) * 100)

