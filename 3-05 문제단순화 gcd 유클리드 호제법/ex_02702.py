from sys import stdin


def get_lcm_gcd(a, b):

    ta, tb = a, b

    if a < b:
        temp = a
    else:
        temp = b

    gcd = 1

    while 1 < temp:
        if a % temp == 0 and b % temp == 0:
            gcd *= temp
            a //= temp
            b //= temp
        temp -= 1

    return ta * tb // gcd, gcd


if __name__ == "__main__":
    n = int(stdin.readline())

    for _ in range(n):
        a, b = map(int, stdin.readline().split())
        ta, tb = get_lcm_gcd(a, b)
        print(ta, tb)
