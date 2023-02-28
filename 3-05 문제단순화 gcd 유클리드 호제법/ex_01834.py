from sys import stdin


if __name__ == "__main__":
    n = int(stdin.readline())
    print((n+1)*n*(n-1)//2)