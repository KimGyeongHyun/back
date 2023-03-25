from sys import stdin


def set_prime(n):
    a = [True for _ in range(n+2)]
    a[0] = False
    a[1] = False
    for i in range(2, int(n**(1/2)) + 1):
        if a[i] is True:
            for j in range(2 * i, n+2, i):
                a[j] = False

    return a


if __name__ == "__main__":
    m, n = map(int, stdin.readline().split())
    a = set_prime(n)

    for i in range(m, n+1):
        if a[i] is True:
            print(i)