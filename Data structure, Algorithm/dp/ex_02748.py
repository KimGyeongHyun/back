from sys import stdin


fib = [0, 1]


def get_fib(n):

    if n <= len(fib) - 1:
        return fib[n]

    for i in range(len(fib), n+1):
        fib.append(fib[i-2] + fib[i-1])

    return fib[n]


if __name__ == "__main__":
    n = int(stdin.readline())
    print(get_fib(n))