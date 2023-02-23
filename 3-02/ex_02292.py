from sys import stdin


if __name__ == "__main__":
    n = int(stdin.readline())
    n -= 1
    n /= 6
    if n%1 != 0:
        n += 1
    n = int(n)
    x = ((1 + 8*n)**(1/2)-1) / 2
    if x%1 != 0:
        x += 1
    x = int(x)
    print(x+1)