from sys import stdin


if __name__ == "__main__":
    t = int(stdin.readline())
    for _ in range(t):
        a, b = map(int, stdin.readline().split(','))
        print(a+b)