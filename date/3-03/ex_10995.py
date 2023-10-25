from sys import stdin


if __name__ == "__main__":
    n = int(stdin.readline())
    for i in range(n):
        if i % 2 == 0:
            for __ in range(n-1):
                print("* ", end="")
            print("*", end="")
        else:
            for __ in range(n):
                print(" *", end="")
        print()