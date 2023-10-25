from sys import stdin
import array as arr


if __name__ == "__main__":
    n, k = map(int, stdin.readline().split())

    l = arr.array('i', [0 for _ in range(5)])

    for _ in range(n):
        s, y = map(int, stdin.readline().split())
        if y <= 2:
            l[0] += 1
        elif y <= 4 and s == 0:
            l[1] += 1
        elif y <= 4 and s == 1:
            l[2] += 1
        elif y <= 6 and s == 0:
            l[3] += 1
        elif y <= 6 and s == 1:
            l[4] += 1

    sum = 0
    for number in l:
        sum += number // k
        if number % k != 0:
            sum += 1

    print(sum)