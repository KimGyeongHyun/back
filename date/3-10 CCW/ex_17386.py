from sys import stdin


if __name__ == "__main__":
    x1, y1, x2, y2 = map(int, stdin.readline().split())
    x3, y3, x4, y4 = map(int, stdin.readline().split())

    # (x1, y1), (x2, y2) 를 지나는 직선 방정식 : y = x * (y2 - y1)/(x2 - x1) + y1 - x1 * (y2 - y1)/(x2 - x1)
    # y = ax + b, y = cx + d 의 교차점 : ((d - b)/(a - c), (a*d - b*c)/(a - c))
    # 주어진 (x, y) 로부터 a, b, c, d 를 계산하고 교차점을 찾아
    # 해당 교차점이 위의 선분을 포함하는지 확인
    # 단 선분이 수직이거나 기울기가 같으면 예외 처리 필요

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

    if x1 == x2 and x3 == x4:
        # print("Case 1 : double vertical")
        print(0)

    elif x1 == x2 or x3 == x4:
        # print("Case 2 : one vertical")
        if x1 == x2:
            mid_y = x1 * (y4 - y3) / (x4 - x3) + y3 - x3 * (y4 - y3)/(x4 - x3)
            # print(x1, mid_y)
            if fly <= mid_y <= fhy:
                print(1)
            else:
                print(0)

        elif x3 == x4:
            mid_y = x3 * (y2 - y1) / (x2 - x1) + y1 - x1 * (y2 - y1)/(x2 - x1)
            # print(x3, mid_y)
            if sly <= mid_y <= shy:
                print(1)
            else:
                print(0)

    else:
        # print("Case 4 : cross")
        a = (y2 - y1)/(x2 - x1)
        b = y1 - x1 * (y2 - y1)/(x2 - x1)
        c = (y4 - y3)/(x4 - x3)
        d = y3 - x3 * (y4 - y3)/(x4 - x3)

        mid_x = (d - b)/(a - c)
        mid_y = (a*d - b*c)/(a - c)
        # print(a, b, c, d)
        # print(mid_x, mid_y)

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

        if flx <= mid_x <= fhx and fly <= mid_y <= fhy and slx <= mid_x <= shx and sly <= mid_y <= shy:
            print(1)
        else:
            print(0)



