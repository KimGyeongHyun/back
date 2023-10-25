from sys import stdin


if __name__ == "__main__":
    n = int(stdin.readline())
    scores = map(int, stdin.readline().split())

    max = 0
    sum = 0

    for score in scores:
        sum += score
        if score > max:
            max = score

    print(sum * 100 / (max * n))
