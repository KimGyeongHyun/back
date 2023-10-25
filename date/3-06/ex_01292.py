from sys import stdin


def easy_prob(a, b):

    sum_number = 1
    count = 1
    sum = 0

    for i in range(1, 1001):
        if b < i:
            break
        if a <= i <= b:
            sum += sum_number
        if sum_number == count:
            count = 1
            sum_number += 1
        else:
            count += 1

    return sum


if __name__ == "__main__":
    a, b = map(int, stdin.readline().split())
    print(easy_prob(a, b))
