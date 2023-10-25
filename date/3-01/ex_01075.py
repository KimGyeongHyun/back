from sys import stdin


if __name__ == "__main__":
    n = int(stdin.readline())
    f = int(stdin.readline())

    n -= n % 100
    a = n // f
    result = a * f
    result %= 100
    if result != 0:
        result += f - 100

    print("{:02d}".format(result))