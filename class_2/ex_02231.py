from sys import stdin


def div_sum(n):
    sum = n
    while n != 0:
        sum += n % 10
        n //= 10

    return sum


def is_have_div_sum(n):
    exp = len(str(n))
    for i in range(int(9 * (10**(exp-2))), n):
        if div_sum(i) == n:
            return i

    return 0


if __name__ == "__main__":
    n = int(stdin.readline())
    result = is_have_div_sum(n)
    if result == 0:
        print(0)
    else:
        print(result)


