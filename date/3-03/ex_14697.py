from sys import stdin


def is_dividable_two(a, b, n):
    num = a
    while num < n:
        if (n-num) % b == 0:
            return True
        num += a

    return False


def is_dividable(a, b, c, n):

    if a == 1 or b == 1 or c == 1:
        return True

    if n % a == 0 or n % b == 0 or n % c == 0:
        return True

    if is_dividable_two(a, b, n) or is_dividable_two(b, c, n) or is_dividable_two(a, c, n):
        return True

    for i in range(1, n//a + 1):
        for j in range(1, n//b + 1):
            for k in range(1, n//c + 1):
                if a*i + b*j + c*k == n:
                    return True

    return False


if __name__ == "__main__":
    a, b, c, n = map(int, stdin.readline().split())
    if is_dividable(a, b, c, n):
        print(1)
    else:
        print(0)
