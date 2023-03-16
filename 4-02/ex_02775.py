from sys import stdin
import array as arr


if __name__ == "__main__":
    t = int(stdin.readline())

    for _ in range(t):
        k = int(stdin.readline())
        n = int(stdin.readline())

        l = [arr.array('i', [0 for _ in range(n)]) for _ in range(k+1)]
        # print(l)

        l[0] = arr.array('i', [i+1 for i in range(n)])

        for i in range(1, k+1):
            for j in range(0, n):
                if j == 0:
                    l[i][j] = l[i-1][j]
                else:
                    l[i][j] = l[i-1][j] + l[i][j-1]

        print(l[k][n-1])
