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


if __name__ == "__main__":
    m, n = map(int, stdin.readline().split())

    for i in range(m, n+1):
        if is_prime(i):
            print(i)