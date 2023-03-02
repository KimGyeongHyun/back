from sys import stdin


if __name__ == "__main__":
    n, t = map(int, stdin.readline().split())

    get_time = None

    for _ in range(n):
        s, i, c = map(int, stdin.readline().split())

        for __ in range(c):
            if t <= s:
                if get_time is None or s < get_time:
                    get_time = s
                    break
            s += i

    if get_time is None:
        print(-1)
    else:
        print(get_time - t)