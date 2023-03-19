from sys import stdin

if __name__ == "__main__":
    n, m = map(int, stdin.readline().split())
    tlist = []
    for _ in range(n):
        tlist.append(str(stdin.readline())[:-1])

    bs = "BWBWBWBW"
    ws = "WBWBWBWB"

    max = 100000000

    for i in range(n-7):
        for j in range(m-7):
            temp_string = []
            for k in range(i, i + 8):
                temp_string.append(tlist[k][j:j+8])

            c1 = 0
            c2 = 0
            for k in range(8):
                for l in range(8):
                    if l%2 == 0:
                        if temp_string[k][l] != bs[k]:
                            c1 += 1
                        if temp_string[k][l] != ws[k]:
                            c2 += 1
                    else:
                        if temp_string[k][l] != ws[k]:
                            c1 += 1
                        if temp_string[k][l] != bs[k]:
                            c2 += 1

            if c1 < c2:
                mid_max = c1
            else:
                mid_max = c2

            if mid_max < max:
                max = mid_max

    print(max)