from sys import stdin


def get_round(n):

    index = 1

    while 1 <= n//10**index:

        num = (n//10**(index-1))%10
        if 5 <= num:
            n += 10**index

        n -= num * 10**(index-1)
        index += 1

    return n


if __name__ == "__main__":
    n = int(stdin.readline())
    print(get_round(n))