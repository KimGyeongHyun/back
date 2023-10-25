from sys import stdin


if __name__ == "__main__":
    n = int(stdin.readline())
    l = []

    for _ in range(n):
        l.append(tuple(map(int, stdin.readline().split())))

    l.sort(key=lambda x: (x[1], x[0]))

    prev_end = -1
    count = 0

    for start, end in l:

        if start < prev_end:
            continue

        if end >= prev_end and start >= prev_end:
            prev_end = end
            count += 1

    print(count)