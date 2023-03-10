from sys import stdin


def CCW(x1, y1, x2, y2, x3, y3):
    """P1 -> P2 -> P3 의 외적을 구해 반시계 : 1, 시계 : -1, 평행 : 0 을 리턴"""
    outer_product = (x2 - x1) * (y3 - y2) - (x3 - x2) * (y2 - y1)
    if outer_product > 0:
        return 1
    elif outer_product < 0:
        return -1
    else:
        return 0


if __name__ == "__main__":
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    x3, y3, x4, y4 = map(int, stdin.readline().split())

    # L1 기준 L2 점 두개의 CCW 를 구함
    first_CCW = CCW(x1, y1, x2, y2, x3, y3)
    second_CCW = CCW(x1, y1, x2, y2, x4, y4)
    # L1 기준 L2 점 두개가 좌우에 있다면 두 개의 CCW 는 부호가 다르다 (1, -1)
    first_cross = first_CCW * second_CCW

    # L2 기준 L1 점 두개의 CCW 를 구함
    first_CCW = CCW(x3, y3, x4, y4, x1, y1)
    second_CCW = CCW(x3, y3, x4, y4, x2, y2)
    # L2 기준 L1 점 두개가 좌우에 있다면 두 개의 CCW 는 부호가 다르다
    second_cross = first_CCW * second_CCW

    # L1 기준 L2 점 두개가 좌우에 있고 L2 기준 L1 점 두개가 좌우에 있다면
    # 두 선분은 교차하게 된다
    # 즉 first_cross 와 second_cross 가 -1이면 두 선분은 교차하게 된다

    # 문제 조건으로 주어진 "점 세개가 같은 직선상에 없다"는 것은
    # 선분을 이루는 네 개의 점은 교차점이 될 수 없다는 것을 의미한다
    # 즉 선분과 선분의 끝점이 만나 교차점을 이룰 수 없다
    # 선분과 선분의 끝점이 만나면 first_cross와 second_cross 가 0이 되고
    # 두 선분은 교차하는 조건을 만족한다
    # 하지만 해당 조건은 불가능하니 값이 0이 되는 조건은 제외한다

    if first_cross == -1 and second_cross == -1:
        print(1)
    else:
        print(0)