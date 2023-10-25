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
    x1, y1 = map(int, stdin.readline().split())
    x2, y2 = map(int, stdin.readline().split())
    x3, y3 = map(int, stdin.readline().split())

    print(CCW(x1, y1, x2, y2, x3, y3))