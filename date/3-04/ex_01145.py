from sys import stdin


def get_lcm(a, b):
    """최소공배수 리턴"""
    if a > b:
        max = a
    else:
        max = b

    gcd = 1
    fa = a
    fb = b

    for i in range(max, 1, -1):
        if a%i == 0 and b%i == 0:
            a = a // i
            b = b // i
            gcd *= i

    return int((fa * fb) / gcd)


def get_lcm_three(a, b, c):
    """3개의 수의 최소공배수 리턴"""
    return get_lcm(a, get_lcm(b, c))


def get_almost(a, b, c, d, e):
    min = get_lcm_three(a, b, c)

    if min > get_lcm_three(a, b, d):
        min = get_lcm_three(a, b, d)

    if min > get_lcm_three(a, b, e):
        min = get_lcm_three(a, b, e)

    if min > get_lcm_three(a, c, d):
        min = get_lcm_three(a, c, d)

    if min > get_lcm_three(a, c, e):
        min = get_lcm_three(a, c, e)

    if min > get_lcm_three(a, d, e):
        min = get_lcm_three(a, d, e)

    if min > get_lcm_three(b, c, d):
        min = get_lcm_three(b, c, d)

    if min > get_lcm_three(b, c, e):
        min = get_lcm_three(b, c, e)

    if min > get_lcm_three(b, d, e):
        min = get_lcm_three(b, d, e)

    if min > get_lcm_three(c, d, e):
        min = get_lcm_three(c, d, e)

    return min


if __name__ == "__main__":
    a, b, c, d, e = map(int, stdin.readline().split())
    print(get_almost(a, b, c, d, e))
