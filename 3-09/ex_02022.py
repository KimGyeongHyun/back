from sys import stdin


def get_guess_width(x, y, c):

    if x < y:
        max = x
    else:
        max = y

    width = max/2
    min = 0

    while True:
        left = (x ** 2 - width ** 2) ** (1 / 2)
        right = (y ** 2 - width ** 2) ** (1 / 2)

        guess_c = left * right / (left + right)

        if -0.0005 <= guess_c - c <= 0.0005:
            return width

        if guess_c < c:
            max -= (max - min) / 2
        else:
            min += (max - min) / 2

        width = (min + max) / 2


if __name__ == "__main__":
    x, y, c = map(float, stdin.readline().split())
    print(get_guess_width(x, y, c))