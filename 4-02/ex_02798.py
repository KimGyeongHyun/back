from sys import stdin
import array as arr


if __name__ == "__main__":
    n, m = map(int, stdin.readline().split())

    l = arr.array('i', list(map(int, stdin.readline().split())))

    min = 0

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                sum = l[i] + l[j] + l[k]
                if min == 0 and sum <= m:
                    min = sum

                if min != 0 and m >= sum > min:
                    min = sum

    print(min)