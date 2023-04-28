from sys import stdin


def get_biggest_dec(n, l):

    dec_l = [0 for _ in range(n)]

    for i in range(n-1, -1, -1):
        if i == n-1:
            dec_l[i] = 1
            continue
        big = 0
        for j in range(n-1, i, -1):
            if l[i] > l[j] and dec_l[j] >= big:
                big = dec_l[j]

        dec_l[i] = big+1

    return max(dec_l)


if __name__ == "__main__":
    n = int(stdin.readline())
    l = list(map(int, stdin.readline().split()))

    print(get_biggest_dec(n, l))
