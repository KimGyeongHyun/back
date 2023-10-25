from sys import stdin

def print_star(n):
    for i in range(n):
        for j in range(n):
            if j % 2 == 0:
                print("*", end="")
            else:
                print(" ", end="")
        print()

        if n == 1:
            return

        for j in range(n):
            if j % 2 == 0:
                print(" ", end="")
            else:
                print("*", end="")
        print()


if __name__ == "__main__":
    n = int(stdin.readline())
    print_star(n)