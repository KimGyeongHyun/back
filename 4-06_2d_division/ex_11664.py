import sys
input = sys.stdin.readline


# 외적
def outer_product(a1, a2, a3, b1, b2, b3):
    return a2 * b3 - a3 * b2, a3 * b1 - a1 * b3, a1 * b2 - a2 * b1


# 내적
def inner_product(a1, a2, a3, b1, b2, b3):
    return a1 * b1 + a2 * b2 + a3 * b3


# 벡터 크기
def size_of_vector(a, b, c):
    return (a**2 + b**2 + c**2) ** (1/2)


if __name__ == "__main__":
    ax, ay, az, bx, by, bz, cx, cy, cz = map(int, input().split())

    # b->a 벡터
    w = [ax-bx, ay-by, az-bz]

    ac = [cx-ax, cy-ay, cz-az]  # a->c
    bc = [cx-bx, cy-by, cz-bz]  # b->c

    # d = size(outer_product(ac, w))/size(w)
    ta, tb, tc = outer_product(ac[0], ac[1], ac[2], w[0], w[1], w[2])
    d = size_of_vector(ta, tb, tc)
    d /= size_of_vector(w[0], w[1], w[2])

    # h : ab 선분을 쭉 이은 직선과 c 와의 최소거리를 구했을 때 교차하는 점
    # h = b + vector(bh)
    # size(vector(bh)) = inner_product(bc, w)/inner_product(w)
    # 크기가 1인 vector bh 의 방향벡터 : w/size(w)
    # vector(bh) = w * inner_product(bc, w)/(inner_product(w)**2)
    # h = b + w * inner_product(bc, w)/(inner_product(w)**2)
    bh = inner_product(bc[0], bc[1], bc[2], w[0], w[1], w[2])
    bh /= size_of_vector(w[0], w[1], w[2]) ** 2
    mid_x = bx + w[0] * bh
    mid_y = by + w[1] * bh
    mid_z = bz + w[2] * bh

    da = size_of_vector(ac[0], ac[1], ac[2])    # ac 벡터 크기
    db = size_of_vector(bc[0], bc[1], bc[2])    # bc 벡터 크기

    # h 가 ab 선분 내부에 있다면 직선과 c의 최단거리가 ab 선분과 c의 최단거리가 된다
    if (ax <= mid_x <= bx or bx <= mid_x <= ax) and (ay <= mid_y <= by or by <= mid_y <= ay) and (az <= mid_z <= bz or bz <= mid_z <= az):
        print(d)
    else:   # h 가 ab 선분 내에 없다면 ac, bc 중 최단거리가 존재한다
        print(min(da, db))
