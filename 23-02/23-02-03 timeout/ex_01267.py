if __name__ == "__main__":
    N = int(input())
    times = map(int, input().split())

    Y, M = 0, 0

    for time in times:
        Y += 10 * (time // 30 + 1)
        M += 15 * (time // 60 + 1)

    if Y > M:
        print('M {}'.format(M))
    elif Y < M:
        print('Y {}'.format(Y))
    else:
        print('Y M {}'.format(Y))