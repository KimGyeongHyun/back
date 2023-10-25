from sys import stdin
import math


if __name__ == "__main__":

    x1, y1 = map(int, stdin.readline().split())
    x2, y2 = map(int, stdin.readline().split())
    x3, y3 = map(int, stdin.readline().split())

    # 탄젠트 역함수를 이용해 점들 간의 각도를 구한다
    # math.atan() : 탄젠트 역함수
    # math.degrees() : angle 을 각도로 변환

    # 수직, 수평의 경우 예외 처리를 한다
    # 0 ~ 90도 까지는 그대로 나온다
    # 90 ~ 180도는 180이 뺄샘 되어서 값이 나오기 때문에 180 을 더한다
    # 탄젠트 역함수의 경우 0 ~ 180도 까지 밖에 도출이 안 되므로
    # 점들 간에 y 값을 비교하여 진행 방향이 아래 쪽이면 180 을 더한다

    # P1 -> P2 의 각도
    if x1 == x2:    # 수직 예외 처리
        if y1 < y2:
            degree1 = 90.0
        else:
            degree1 = 270.0
    elif y1 == y2:    # 수평 예외 처리
        if x1 < x2:
            degree1 = 0.0
        else:
            degree1 = 180.0

    else:
        degree1 = math.degrees(math.atan((y2 - y1) / (x2 - x1)))
        if degree1 < 0:     # 90 ~ 180 인 경우
            degree1 += 180.0
        if y2 - y1 < 0:     # 진행 방향이 아래 쪽인 경우
            degree1 += 180.0

    # P2 -> P3 의 각도
    if x2 == x3:
        if y2 < y3:
            degree2 = 90.0
        else:
            degree2 = 270.0
    elif y2 == y3:
        if x2 < x3:
            degree2 = 0.0
        else:
            degree2 = 180.0

    else:
        degree2 = math.degrees(math.atan((y3 - y2) / (x3 - x2)))
        if degree2 < 0:
            degree2 += 180.0
        if y3 - y2 < 0:
            degree2 += 180.0

    # 직선
    if degree1 == degree2 or degree1 + 180 == degree2 or degree1 == degree2 + 180:
        print(0)
    # 반시계
    elif 0 < (degree2 - degree1) % 360 < 180:
        print(1)
    # 시계
    else:
        print(-1)