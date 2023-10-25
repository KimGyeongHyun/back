from sys import stdin


def get_sum_number(c, n):
    if n <= len(c) - 1:
        return c[n]

    for i in range(len(c), n+1):
        c.append(c[i-3] + c[i-2] + c[i-1])

    return c[n]


if __name__ == "__main__":
    c = [0, 1, 2, 4]
    t = int(stdin.readline())

    for _ in range(t):
        print(get_sum_number(c, int(stdin.readline())))
