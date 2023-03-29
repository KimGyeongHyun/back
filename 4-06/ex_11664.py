import sys
input = sys.stdin.readline


def outer_product(a1, a2, a3, b1, b2, b3):
    return a2 * b3 - a3 * b2, a3 * b1 - a1 * b3, a1 * b2 - a2 * b1


def inner_product(a1, a2, a3, b1, b2, b3):
    return a1 * b1 + a2 * b2 + a3 * b3


def size_of_vector(a, b, c):
    return (a**2 + b**2 + c**2) ** (1/2)


if __name__ == "__main__":
    ax, ay, az, bx, by, bz, cx, cy, cz = map(int, input().split())
    w = [ax-bx, ay-by, az-bz]

    ac = [cx-ax, cy-ay, cz-az]
    bc = [cx-bx, cy-by, cz-bz]
    ta, tb, tc = outer_product(ac[0], ac[1], ac[2], w[0], w[1], w[2])
    d = size_of_vector(ta, tb, tc)
    d /= size_of_vector(w[0], w[1], w[2])
    da = size_of_vector(ac[0], ac[1], ac[2])
    db = size_of_vector(bc[0], bc[1], bc[2])

    bh = inner_product(bc[0], bc[1], bc[2], w[0], w[1], w[2])
    bh /= size_of_vector(w[0], w[1], w[2]) ** 2
    mid_x = bx + w[0] * bh

    print(ax, bx, mid_x)

    if ax <= mid_x <= bx:
        print(d)
    else:
        print(min(da, db))

    print()
    print(d)
    print(da)
    print(db)



