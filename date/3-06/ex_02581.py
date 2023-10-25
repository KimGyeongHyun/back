from sys import stdin


def sosu(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    m = int(stdin.readline())
    n = int(stdin.readline())
    min = 0
    sum = 0
    for i in range(m, n+1):
        if sosu(i):
            if min == 0:
                min = i
            sum += i

    if min == 0:
        print(-1)
    else:
        print(sum)
        print(min)