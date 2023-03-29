def star_blank():
    print("* ", end="")


def blank_star():
    print(" *", end="")


def print_star(n):
    for _ in range(n):
        print("*", end="")


def print_blank(n):
    for _ in range(n):
        print(" ", end="")


def up_star(n):
    if n == 1:
        return

    for i in range(1, 2 * n):
        t = 4 * n - 1
        if i == 1:
            print_star(t - 2)
        else:
            for _ in range(i//2):
                star_blank()
            if i % 2 == 0 and i != 2:
                print_blank(t - i//2 * 4)
            if i % 2 != 0:
                print_star(t - i//2 * 4)

            for _ in range(i//2 - 1):
                blank_star()

        print()


def middle_star(n):
    for _ in range(n-1):
        star_blank()
    print("*", end="")
    for _ in range(n-1):
        blank_star()
    print()


def donw_star(n):
    if n == 1:
        return

    for i in range(2 * n - 1):
        for _ in range(n - 1 - i//2):
            star_blank()

        if i % 2 == 0:
            print_star(2 * i + 1)
        else:
            print_blank(2 * i - 1)

        for _ in range(n - 1 - i // 2):
            blank_star()

        print()


if __name__ == "__main__":
    n = int(input())
    up_star(n)
    middle_star(n)
    donw_star(n)