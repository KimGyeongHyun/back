from sys import stdin


def is_prime(n):

    if n == 2:
        return True

    if n == 1 or n % 2 == 0:
        return False

    for i in range(3, int(n**(1/2)) + 1, 2):
        if n%i == 0:
            return False

    return True


def set_prime_eratos(n):
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

    for i in range(m, n+1):
        if is_prime(i):
            print(i)