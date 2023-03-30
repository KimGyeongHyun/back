import sys
input = sys.stdin.readline
MAX_REPEAT = 100

# 삼분 탐색이라는 방법을 문제 내 알고리즘 분류 항목에서 찾았으며
# 이를 이용하여 최단거리를 계산할 예정

# 탈출 조건을 x값만 비교해서 했으나 x가 같은 선상에 있는 경우
# 점들의 x가 같을 때 문제가 생긴다
# 따라서 mid1, mid2 의 거리가 짧을 때로 탈출하게 했다

# 삼분 탐색으로 start = end 이 될 때까지 반복 (float 차이가 없어질 때까지 반복)
# 그러면 mid1 의 점은 float 의 표현의 한계에서 제일 가까운 점을 찾아낸 것과 같다
# 위의 방법으로 시도해본 결과 특정 환경에선 start = end 가 성립하지 않고 무한 루프에 들어간다

# 최대 순환을 어느정도로 둘지는 길이가 10000 * sqrt(2) 인 극단적인 상황에서 삼분 탐색할 때에 맞춰야 한다
# 계산 결과 70 이상일 때 1e-6 아래까지 수렴하는 것으로 확인 되었다 ( (2/3) ** (70) < e-12 )
# start = end 라는 식 대신 반복을 100번 이상 하면 거리는 오차 범위 1e-6 아래로 수렴할 것이다

# 삼분 탐색 안에 ac, bc 의 길이가 최소일 때 해당 길이를 추출하고 탈출하는 필요없는 조건문이 있었다
# 해당 조건문을 삭제하니 제대로 동작했다


def get_length(a, b, c):
    return (a**2 + b**2 + c**2) ** (1/2)


if __name__ == "__main__":
    ax, ay, az, bx, by, bz, cx, cy, cz = map(int, input().split())
    length = 0
    count = 0

    while True:

        count += 1

        mid1 = [(2 * ax + bx)/3, (2 * ay + by)/3, (2 * az + bz)/3]
        mid2 = [(ax + 2 * bx)/3, (ay + 2 * by)/3, (az + 2 * bz)/3]

        al = get_length(ax-cx, ay-cy, az-cz)
        bl = get_length(bx-cx, by-cy, bz-cz)
        mid1l = get_length(mid1[0]-cx, mid1[1]-cy, mid1[2]-cz)
        mid2l = get_length(mid2[0]-cx, mid2[1]-cy, mid2[2]-cz)

        if count >= 100:
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

    print("{:.10f}".format(length))
