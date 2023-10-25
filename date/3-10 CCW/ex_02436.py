from sys import stdin


def get_gcd(x, y):

    if y == 0:
        return x
    else:
        return get_gcd(y, x % y)


def is_gcd_lcm(x, y, input_gcd, input_lcm):
    gcd = get_gcd(x, y)
    lcm = int(x * y / gcd)
    if gcd == input_gcd and lcm == input_lcm:
        return True
    return False


if __name__ == "__main__":
    gcd, lcm = map(int, stdin.readline().split())

    mid = (gcd * lcm) ** (1/2)

    mid = int(mid) + 1

    while True:

        mid -= 1

        if mid % gcd == 0 and lcm % mid == 0:
            big = gcd * lcm / mid
            if big % 1 != 0:
                continue
            big = int(big)

            if is_gcd_lcm(mid, big, gcd, lcm):
                break

    print("{} {}".format(mid, big))