import sys

input = sys.stdin.readline


if __name__ == "__main__":

    while True:
        l = list(map(int, input().split()))

        if len(l) == 1:
            break

        b = l[1:]
        n = l[0]
        res = []

        for i in range(n-5):
            for j in range(i+1, n-4):
                for k in range(j+1, n-3):
                    for m in range(k+1, n-2):
                        for p in range(m+1, n-1):
                            for q in range(p+1, n):
                                tl = [str(b[i]), str(b[j]), str(b[k]), str(b[m]), str(b[p]), str(b[q])]
                                res.append(" ".join(tl))

        for line in res:
            print(line)
        print()