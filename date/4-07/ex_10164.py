import sys
input = sys.stdin.readline


factorial_list = [1]


def factorial(n):

    if n <= len(factorial_list):
        return factorial_list[n-1]

    value = n * factorial(n-1)
    factorial_list.append(value)
    return value


def combination(n, r):
    # print("move :", n, ", index :", r)

    if n <= 1 or n == r or r == 0:
        return 1

    return factorial(n) // (factorial(r) * factorial(n-r))


if __name__ == "__main__":
    n, m, k = map(int, input().split())

    if k == 0:
        k = 1

    x, y = (k-1) % m, (k-1) // m

    value = combination(x+y, x) * combination(m+n - 2 - x - y, m-x-1)

    print(value)
