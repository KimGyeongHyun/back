from sys import stdin


def is_possible(n):
    count = n // 5

    for i in range(0, 3):
        if count - i < 0:
            return -1
        if (n - 5 * (count - i)) % 3 == 0:
            count += (n - 5 * (count - i)) // 3 - i
            break

    return count


if __name__ == "__main__":
    n = int(stdin.readline())
    print(is_possible(n))