from sys import stdin
import time


def is_prime(n):
    if n == 1:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1

    return True


if __name__ == "__main__":
    result = ''

    start = time.time()
    count = 1

    # while True:
    while count <= 100000:

        # n = int(stdin.readline())
        n = 1000000

        if n == 0:
            break

        for i in range(3, n, 2):
            if is_prime(i) and is_prime(n - i):
                result += f'{n} = {i} + {n-i}\n'
                break

        count += 1

    print(result)
    print(time.time() - start)