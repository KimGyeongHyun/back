def first_fest(a):
    number = 1
    repeat = 1

    if a == 0:
        return 0

    if a <= number:
        return 500_0000
    repeat += 1
    number += repeat

    if a <= number:
        return 300_0000
    repeat += 1
    number += repeat

    if a <= number:
        return 200_0000
    repeat += 1
    number += repeat

    if a <= number:
        return 50_0000
    repeat += 1
    number += repeat

    if a <= number:
        return 30_0000
    repeat += 1
    number += repeat

    if a <= number:
        return 10_0000

    return 0


def second_fest(a):
    number = 1
    repeat = 1

    if a == 0:
        return 0

    if a <= number:
        return 512_0000
    repeat *= 2
    number += repeat

    if a <= number:
        return 256_0000
    repeat *= 2
    number += repeat

    if a <= number:
        return 128_0000
    repeat *= 2
    number += repeat

    if a <= number:
        return 64_0000
    repeat *= 2
    number += repeat

    if a <= number:
        return 32_0000

    return 0


if __name__ == "__main__":
    T = int(input())

    for _ in range(T):
        a, b = map(int, input().split())

        print(first_fest(a) + second_fest(b))