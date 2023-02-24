from sys import stdin


if __name__ == "__main__":
    a, b, v = map(int, stdin.readline().split())
    c = (v-a) / (a-b)
    if c%1 != 0:
        c += 1
    print(int(c) + 1)
