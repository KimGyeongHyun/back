from sys import stdin


def draw_number(n):

    div = 1
    div_number = 1
    count = 0

    while True:
        if n//(10*div) == 0:
            count += div_number * (n - div + 1)
            return count

        count += div_number * div * 9
        div *= 10
        div_number += 1


if __name__ == "__main__":
    n = int(stdin.readline())
    print(draw_number(n))