import sys
input = sys.stdin.readline


if __name__ == "__main__":
    f = input()
    s = input()

    # f 가 짧은 문자열

    if len(f) > len(s):
        temp = s[:]
        s = f
        f = temp

    n = len(f)-1

    dp = [None for _ in range(n+1)]

    for i in range(1, n+1):
