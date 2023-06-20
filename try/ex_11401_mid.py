import sys


def set_prime(n):
    a = [True for _ in range(n+2)]
    a[0] = False
    a[1] = False
    for i in range(2, int(n**(1/2)) + 1):
        if a[i] is True:
            for j in range(2 * i, n+2, i):
                a[j] = False

    return a


def factorial(n):

    res = 1
    for i in range(1, n+1):
        res *= i

    return res


if __name__ == "__main__":
    flags = set_prime(31622)
    primes = []
    for i in range(1, 31623):
        if flags[i]:
            primes.append(i)

    exp = [0 for _ in range(len(primes))]

    n, k = map(int, sys.stdin.readline().split())

    temp = factorial(n)
    temp //= factorial(n-k)
    temp //= factorial(k)
    temp %= 1000000007

    print(temp)
