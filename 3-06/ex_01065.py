from sys import stdin


def is_arithmetic(n):

    if n < 100:
        return True

    a = n//100
    b = (n//10)%10
    c = n%10

    if a-b == b-c:
        return True

    return False


if __name__ == "__main__":
    n = int(stdin.readline())
    count = 0
    for i in range(1, n+1):
        if (is_arithmetic(i)):
            count += 1
    print(count)