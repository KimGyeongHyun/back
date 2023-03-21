from sys import stdin


def up_down(n):
    gap = 2 * n - 3

    temp_string = ""

    for _ in range(n):
        temp_string += '*'
    for _ in range(gap):
        temp_string += ' '
    for _ in range(n):
        temp_string += '*'

    return temp_string


def gap_star(n):
    temp_string = '*'
    for _ in range(n-2):
        temp_string += ' '
    temp_string += '*'

    return temp_string


def middle(n):
    temp_string = ""
    for _ in range(n-1):
        temp_string += ' '
    temp_string += gap_star(n)
    for _ in range(n-2):
        temp_string += ' '
    temp_string += '*'

    return temp_string


if __name__ == "__main__":

    n = int(stdin.readline())
    print(up_down(n))
    for i in range(n-2, 0, -1):
        for j in range((n-1) - i):
            print(' ', end='')
        print(gap_star(n), end='')
        for j in range(2 * i - 1):
            print(' ', end='')
        print(gap_star(n))

    print(middle(n))

    for i in range(1, n-1):
        for j in range((n-1) - i):
            print(' ', end='')
        print(gap_star(n), end='')
        for j in range(2 * i - 1):
            print(' ', end='')
        print(gap_star(n))

    print(up_down(n))