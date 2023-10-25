from sys import stdin


def get_factorial_two_five(n):

    five = 0
    two = 0
    temp = n

    while True:
        if n // 2 == 0:
            break
        n //= 2
        two += n

    n = temp

    while True:
        if n//5 == 0:
            break
        n //= 5
        five += n

    return two, five


if __name__ == "__main__":
    n, m = map(int, stdin.readline().split())
    two, five = get_factorial_two_five(n)

    ttwo, tfive = get_factorial_two_five(m)
    two -= ttwo
    five -= tfive

    ttwo, tfive = get_factorial_two_five(n-m)
    two -= ttwo
    five -= tfive

    if two < five:
        print(two)
    else:
        print(five)

