from sys import stdin


def triangle_v(x1, y1, x2, y2, x3, y3):
    """
    세 개의 점을 외적을 통해 삼각형 넓이를 구하여 리턴
    세 개의 점의 방향성을 가져오기 위해 삼각형 넓이에 절대값을 취하지 않고 리턴
    """
    outer_product = (x2 - x1) * (y3 - y2) - (x3 - x2) * (y2 - y1)
    return outer_product/2


if __name__ == "__main__":
    n = int(stdin.readline())
    fx, fy = None, None     # 첫번째 점
    sx, sy = None, None     # 두번째 점
    total_v = 0.0           # 총 넓이

    # 만약 다각형의 모양이 볼록하다면
    # 외적으로 삼각형의 넓이를 양수로 리턴하여 모두 더하면 된다
    # 하지만 다각형의 모양이 오목하다면 위의 방법은 통하지 않는다

    # 대신 CWW 개념을 도입하여 P1 -> P2 -> P3 의 시계, 반시계 방향에 따라
    # 삼각형 넓이에 부호를 다르게 준다
    # 즉 외적/2 는 삼각형 넓이에 CWW 정보가 부호로 담겨있게 된다

    # 만약 다각형이 시계 방향으로 구성된다면
    # 시계 방향의 삼각형 넓이는 더해지고 반시계 방향의 삼각형 넓이는 빼진다
    # 다각형이 반시계 방향으로 구성된다면
    # 반시계 방향의 삼각형 넓이는 더해지고 시계 방향의 삼각형 넓이 는 빼진다
    # 즉 다각형의 넓이는 CCW 정보가 부호로 담긴 삼각형 넓이 총합의 절대값이다

    for i in range(1, n+1):
        x, y = map(int, stdin.readline().split())
        if i == 1:
            fx, fy = x, y
        elif i == 2:
            sx, sy = x, y
        else:
            tx, ty = x, y
            total_v += triangle_v(fx, fy, sx, sy, tx, ty)
            sx, sy = x, y

    # 다각형이 시계 방향으로 구성되어 넓이가 -가 나왔다면 양수로 바꾼다
    if total_v < 0:
        total_v = -1 * total_v

    print("{:.1f}".format(total_v))