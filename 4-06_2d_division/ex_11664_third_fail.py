import sys
input = sys.stdin.readline

# 외적과 내적을 이용해서 예제 문제를 모두 풀었으나,
# float 특성상 정답 오차범위 10e-6 에 들어가지 못하여 채점에서 틀렸다
# http://boj.kr/2d43574fffef4bc384c587e840cf03c4

# 삼분 탐색이라는 방법을 문제 내 알고리즘 분류 항목에서 찾았으며
# 이를 이용하여 최단거리를 계산할 예정이다

# 탈출 조건을 x값만 비교해서 했으나 x가 같은 선상에 있는 경우
# 점들의 x가 같을 때 문제가 생긴다
# 따라서 mid1, mid2 의 거리가 짧을 때로 탈출하게 했다


def get_length(a, b, c):
    return (a**2 + b**2 + c**2) ** (1/2)


if __name__ == "__main__":
    ax, ay, az, bx, by, bz, cx, cy, cz = map(int, input().split())
    length = 0

    while True:

        mid1 = [(2 * ax + bx)/3, (2 * ay + by)/3, (2 * az + bz)/3]
        mid2 = [(ax + 2 * bx)/3, (ay + 2 * by)/3, (az + 2 * bz)/3]

        al = get_length(ax-cx, ay-cy, az-cz)
        bl = get_length(bx-cx, by-cy, bz-cz)
        mid1l = get_length(mid1[0]-cx, mid1[1]-cy, mid1[2]-cz)
        mid2l = get_length(mid2[0]-cx, mid2[1]-cy, mid2[2]-cz)

        print(ax, mid1[0], mid2[0], bx)
        print(al, mid1l, mid2l, bl)
        print(ax, ay, az)
        print(mid2[0], mid2[1], mid2[2])
        print(mid2[0], mid2[1], mid2[2])
        print(bx, by, bz)
        print()

        if al < min(mid1l, min(mid2l, bl)):
            length = al
            break

        if bl < min(mid1l, min(mid2l, al)):
            length = bl
            break

        if get_length(mid1[0]-mid2[0], mid1[1]-mid2[1], mid1[2]-mid2[2]) < 0.0000000001:
            length = (mid1l + mid2l) / 2
            break

        if mid1l > mid2l:
            ax = mid1[0]
            ay = mid1[1]
            az = mid1[2]
        else:
            bx = mid2[0]
            by = mid2[1]
            bz = mid2[2]

    print(length)
