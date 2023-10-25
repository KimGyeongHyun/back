from sys import stdin


def draw_star(n):

    n -= 1

    for i in range(0, 2*n):
        for _ in range((i + 1) // 2):
            print("* ", end="")

        if i%2 == 0:
            for _ in range(1 + 4 * (n - i//2)):
                print("*", end="")
        else:
            for _ in range(1 + 4 * (n - (i+1)//2)):
                print(" ", end="")

        for _ in range((i + 1) // 2):
            print(" *", end="")

        print()

    for _ in range(n):
        print("* ", end="")
    print("*", end="")
    for _ in range(n):
        print(" *", end="")
    print()

    for i in range(2*n-1, -1, -1):
        for _ in range((i + 1) // 2):
            print("* ", end="")

        if i%2 == 0:
            for _ in range(1 + 4 * (n - i//2)):
                print("*", end="")
        else:
            for _ in range(1 + 4 * (n - (i+1)//2)):
                print(" ", end="")

        for _ in range((i + 1) // 2):
            print(" *", end="")

        print()



if __name__ == "__main__":
    n = int(stdin.readline())
    draw_star(n)