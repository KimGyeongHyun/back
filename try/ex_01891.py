import sys
input = sys.stdin.readline


def get_xy(nd, input_num):

    dx = 0
    dy = 0

    for i in range(nd):
        mn = (input_num//(10**i)) % 10

        if mn == 1 or mn == 4:
            dx += 2 ** i
        if mn == 1 or mn == 2:
            dy += 2 ** i

    return dx, dy


def get_fourth(nd, input_dx, input_dy):

    texp = 2 ** nd

    if input_dx < 0 or texp <= input_dx:
        return -1
    if input_dy < 0 or texp <= input_dy:
        return -1

    res = 0

    for i in range(nd):

        exp = 10 ** i

        if input_dx & (2 ** i) == 2 ** i:
            if input_dy & (2 ** i) == 2 ** i:
                res += exp
            else:
                res += 4 * exp
        else:
            if input_dy & (2 ** i) == 2 ** i:
                res += 2 * exp
            else:
                res += 3 * exp

    return res


if __name__ == "__main__":

    d, f = map(int, input().split())
    x, y = map(int, input().split())

    dx, dy = get_xy(d, f)

    dx += x
    dy += y

    print(get_fourth(d, dx, dy))