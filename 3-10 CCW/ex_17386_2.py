from sys import stdin


def is_met(x1, y1, x2, y2, x3, y3, x4, y4):

    # y = ax + b 의 직선 방정식으로 선분의 직선을 도출한다
    # 두 직선의 교차점을 구한다
    # 해당 교차점이 선분 범위 내에 있으면 두 선분은 만난다고 볼 수 있다

    # 기울기가 수직이라면 y = ax + b 의 방정식을 도출할 수 없다
    # 따라서 두 선분중 하나라도 기울기가 수직이라면 예외처리를 해야 한다

    # 세 점이 일직선 위에 있는 경우는 없다
    # 그 말은 두 선분의 기울기가 같으면 같은 직선상에 있을 수 없다는 얘기이다
    # 즉 두 선분의 기울기가 같으면 만나지 않는다

    # 알고리즘 순서
    # L1 또는 L2 의 기울기가 수직일 때 예외 처리
    # y = ax + b, y = cx + d 도출
    # 두 직선의 기울기가 같으면 예외 처리
    # a, b, c, d 로 교차점 찾음
    # 교차점이 L1, L2 범위 내부에 있는지 확인

    # L1, L2 둘 다 수직인 경우 교차 불가
    if x1 == x2 and x3 == x4:
        return 0

    # y 대소 구분
    if y1 < y2:
        fly = y1
        fhy = y2
    else:
        fly = y2
        fhy = y1

    if y3 < y4:
        sly = y3
        shy = y4
    else:
        sly = y4
        shy = y3

    # 한 선분이 수직인 경우
    # 교차점을 찾아 수직인 선분 안에 교차점이 있는지 확인
    if x1 == x2 or x3 == x4:
        if x1 == x2:
            mid_y = x1 * (y4 - y3) / (x4 - x3) + y3 - x3 * (y4 - y3)/(x4 - x3)
            if fly < mid_y < fhy:
                return 1
            else:
                return 0

        elif x3 == x4:
            mid_y = x3 * (y2 - y1) / (x2 - x1) + y1 - x1 * (y2 - y1)/(x2 - x1)
            if sly < mid_y < shy:
                return 1
            else:
                return 0

    # L1 -> y = ax + b / L2 -> y = cx + d
    a = (y2 - y1) / (x2 - x1)
    b = y1 - x1 * (y2 - y1) / (x2 - x1)
    c = (y4 - y3) / (x4 - x3)
    d = y3 - x3 * (y4 - y3) / (x4 - x3)

    # 기울기가 같은 경우 교차 불가
    if a == c:
        return 0

    # 교차점
    mid_x = (d - b) / (a - c)
    mid_y = (a * d - b * c) / (a - c)

    # a, b, c, d 와 교차점 확인
    # print(a, b, c, d)
    # print(mid_x, mid_y)

    # x 대소 구분
    if x1 < x2:
        flx = x1
        fhx = x2
    else:
        flx = x2
        fhx = x1

    if x3 < x4:
        slx = x3
        shx = x4
    else:
        slx = x4
        shx = x3

    # 보통의 경우 교차점의 x, y는  점 4개의 x, y 와 일치하지 않는다
    # 점 4개 중 하나가 교차점이라면 3 개의 점이 같은 직선상에 있게 되기 때문이다
    # 따라서 비교식에 =를 넣을 필요가 없다 (넣어도 오류가 없고 애초에 같을 수가 없다)
    # 하지만 기울기가 수평이라면 교차점의 y는 기울기가 수평인 y 값과 같게 된다
    # 따라서 비교식에 =를 넣었다

    # 선분 내부에 교차점이 있다면 두 선분은 교차
    if flx < mid_x < fhx and fly <= mid_y <= fhy and slx < mid_x < shx and sly <= mid_y <= shy:
        return 1
    else:   # 아니면 교차 아님
        return 0


if __name__ == "__main__":
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    x3, y3, x4, y4 = map(int, stdin.readline().split())

    print(is_met(x1, y1, x2, y2, x3, y3, x4, y4))

