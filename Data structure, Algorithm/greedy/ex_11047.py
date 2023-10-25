from sys import stdin


if __name__ == "__main__":
    n, k = map(int, stdin.readline().split())

    coin_list = []
    for _ in range(n):
        coin_list.append(int(stdin.readline()))

    coin_list.reverse()

    count = 0

    for coin in coin_list:
        mid_count = k // coin
        k -= mid_count * coin
        count += mid_count

    print(count)
