from sys import stdin


def return_year(M, N, x, y):
    for year in range(x, M * N + 1, M):
        if year % N == y % N and x <= year and y <= year:
            return year

    return -1


if __name__ == "__main__":
    t = int(stdin.readline())

    for _ in range(t):
        M, N, x, y = map(int, stdin.readline().split())

        print(return_year(M, N, x, y))

