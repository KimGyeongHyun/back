from sys import stdin


def get_low_eight_number(l, r):
    ldiv = 10
    rdiv = 10

    while l//ldiv != 0:
        ldiv *= 10

    while r//rdiv != 0:
        rdiv *= 10

    if ldiv != rdiv:
        return 0

    count = 0
    div = ldiv//10
    while l//div == r//div:
        if l//div == 8:
            count += 1
        l -= l//div * div
        r -= r//div * div
        div //= 10
        if div == 0:
            break

    return count


if __name__ == "__main__":
    l, r = map(int, stdin.readline().split())
    print(get_low_eight_number(l, r))
