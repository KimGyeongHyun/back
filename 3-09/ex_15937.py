from sys import stdin


if __name__ == "__main__":
    fx1, fy1, fx2, fy2 = map(int, stdin.readline().split())
    sx1, sy1, sx2, sy2 = map(int, stdin.readline().split())

    #  Q
    # P
    if fx2 == sx1 and fy2 == sy1:
        print("POINT")

    # P
    #  Q
    elif fx2 == sx1 and fy1 == sy2:
        print("POINT")

    #  P
    # Q
    elif fx1 == sx2 and fy1 == sy2:
        print("POINT")

    # Q
    #  P
    elif fx1 == sx2 and fy2 == sy1:
        print("POINT")

    # PQ, QP
    elif (fx2 == sx1 or fx1 == sx2) and fy1 < sy2 and fy2 > sy1:
        print("LINE")

    # P, Q
    # Q, P
    elif (fy1 == sy2 or fy2 == sy1) and fx1 < sx2 and fx2 > sx1:
        print("LINE")

    elif fx1 < sx2 and fx2 > sx1 and fy1 < sy2 and fy2 > sy1:
        print("FACE")

    else:
        print("NULL")
