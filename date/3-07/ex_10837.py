from sys import stdin


def is_possible(k, m, n):

    if m > n:
        remain = k - m + 1
        if remain < m - n - 1:
            return False
    elif m < n:
        remain = k - n
        if remain < n - m - 1:
            return False

    return True


if __name__ == "__main__":
    k = int(stdin.readline())
    c = int(stdin.readline())
    for _ in range(c):
        m, n = map(int, stdin.readline().split())
        if is_possible(k, m, n):
            print(1)
        else:
            print(0)
