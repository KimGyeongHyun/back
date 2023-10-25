import sys
input = sys.stdin.readline


count = 0
l = []


def hanoi(n, start, mid, end):

    global count, l
    count += 1

    if n == 1:
        l.append((start, end))

    else:
        hanoi(n-1, start, end, mid)
        l.append((start, end))
        hanoi(n-1, mid, start, end)


if __name__ == "__main__":
    n = int(input())
    hanoi(n, 1, 2, 3)
    print(count)
    for items in l:
        print(items[0], items[1])