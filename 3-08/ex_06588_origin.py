from sys import stdin


def isPrime(n):
    if n == 1:
        return False

    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


result = ''
while True:
    n = int(stdin.readline())
    if n == 0:
        break

    for i in range(3, n, 2):
        if isPrime(i) and isPrime(n - i):
            result += f'{n} = {i} + {n - i}\n'
            break

print(result)