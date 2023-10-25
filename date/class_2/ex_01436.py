from sys import stdin


if __name__ == "__main__":
    n = int(stdin.readline())
    count = 0
    start = 665

    while True:

        if n == count:
            break

        start += 1

        start_str = str(start)
        for i in range(len(start_str)-2):
            if start_str[i:i+3] == "666":
                count += 1
                break

    print(start)
