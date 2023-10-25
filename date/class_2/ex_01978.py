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
    n = int(stdin.readline())
    l = list(map(int, stdin.readline().split()))
    count = 0
    for number in l:
        if is_prime(number):
            count += 1

    print(count)