from sys import stdin


def get_kth_number(n, k):
    div = 1
    exp = 1

    while n//div != 0:

        if 9 * div * exp < k:
            k -= 9 * div * exp
            div *= 10
            exp += 1

        else:
            if (n - div + 1) * exp < k:
                break

            th1 = (k-1) // exp + div
            th2 = (k-1) % exp
            th2 = exp - th2 - 1

            return th1//(10**th2) % 10

    return -1


if __name__ == "__main__":
    n, k = map(int, stdin.readline().split())
    print(get_kth_number(n, k))
