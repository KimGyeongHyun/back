from sys import stdin


if __name__ == "__main__":
    x = int(stdin.readline())

    i = 64
    count = 0
    while 1 <= i:
        if i <= x:
            x -= i
            count += 1
        i //= 2

    print(count)