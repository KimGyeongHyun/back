from sys import stdin


if __name__ == "__main__":
    hurt_finger = int(stdin.readline())
    countable = int(stdin.readline())
    count = 0

    if hurt_finger == 1:
        count = 8 * countable

    elif hurt_finger == 5:
        count = 8 * countable + 4

    else:
        count = countable//2 * 8
        if countable%2 == 0:
            count += hurt_finger - 1
        else:
            count += 9 - hurt_finger

    print(count)