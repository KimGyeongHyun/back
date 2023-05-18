from sys import stdin


if __name__ == "__main__":
    str = stdin.readline().strip()

    count = 1
    cur = str[0]

    for i in range(1, len(str)):
        if cur == str[i]:
            continue
        cur = str[i]
        count += 1

    print(count//2)