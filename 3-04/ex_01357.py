from sys import stdin


def rev(n):
    if n < 10:
        return n
    elif n < 100:
        return (n%10) * 10 + n//10
    elif n < 1000:
        return (n%10) * 100 + ((n//10)%10) * 10 + n//100
    elif n < 10000:
        return (n%10) * 1000 + ((n//10)%10) * 100 + ((n//100)%10) * 10 + n//1000

    return 0


if __name__ == "__main__":
    x, y = map(int, stdin.readline().split())
    print(rev(rev(x) + rev(y)))