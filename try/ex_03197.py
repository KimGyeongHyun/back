import sys
from collections import deque
# from my_lib.tools import *
import copy
input = sys.stdin.readline

# 풀이 1
# 백조가 만나는지 확인하고 만나지 않으면 빙판을 갱신, 반복
# 시간초과 발생

if __name__ == "__main__":
    r, c = map(int, input().split())
    lx1, ly1, lx2, ly2 = -1, -1, 0, 0
    water = [[False for _ in range(c)] for _ in range(r)]
    for i in range(r):
        tstr = input().strip()
        for j in range(c):
            if tstr[j] == ".":
                water[i][j] = True
            if tstr[j] == "L":
                if lx1 == -1:
                    lx1, ly1 = j, i
                else:
                    lx2, ly2 = j, i
                water[i][j] = True

    w = 0
    flag = False
    while True:
        visit = [[False for _ in range(c)] for _ in range(r)]
        d = deque()
        d.append((lx1, ly1))

        while d:
            x, y = d.popleft()
            # print("first", x, y)
            if visit[y][x]:
                continue
            visit[y][x] = True
            if x == lx2 and y == ly2:
                print(w)
                exit()
            if 1 <= x and water[y][x-1]:
                d.append((x-1, y))
            if x < c-1 and water[y][x+1]:
                d.append((x+1, y))
            if 1 <= y and water[y-1][x]:
                d.append((x, y-1))
            if y < r-1 and water[y+1][x]:
                d.append((x, y+1))

        w += 1

        visit = [[False for _ in range(c)] for _ in range(r)]
        t_water = copy.deepcopy(water)

        for i in range(r):
            for j in range(c):

                # print("start with >>>>>>>>>>>>>>>", j, i)

                if visit[i][j]:
                    continue
                if not water[i][j]:
                    continue

                d.append((j, i))
                while d:
                    x, y = d.popleft()
                    # print("second", x, y)
                    if visit[y][x]:
                        continue
                    visit[y][x] = True
                    if 1 <= x:
                        if water[y][x - 1]:
                            d.append((x - 1, y))
                        else:
                            t_water[y][x-1] = True
                    if x < c - 1:
                        if water[y][x+1]:
                            d.append((x+1, y))
                        else:
                            t_water[y][x+1] = True
                    if 1 <= y:
                        if water[y-1][x]:
                            d.append((x, y-1))
                        else:
                            t_water[y-1][x] = True
                    if y < r-1:
                        if water[y+1][x]:
                            d.append((x, y+1))
                        else:
                            t_water[y+1][x] = True

        water = copy.deepcopy(t_water)
        # print("after water")
        # print_2d_array_01(water)
