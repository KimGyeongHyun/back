from sys import stdin

if __name__ == "__main__":
    a, b, c = map(int, stdin.readline().split())
    print((a+b)%c)
    print(((a%c) + (b%c))%c)
    print((a*b)%c)
    print(((a%c) * (b%c))%c)

