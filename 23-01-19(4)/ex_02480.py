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

