import sys
from my_lib.tools import print_list_pretty
sys.setrecursionlimit(10**7)
input = sys.stdin.readline


def find(x):

    if x == -1:
        return -1

    if par[x] == x:
        return x
    par[x] = find(par[x])

    return par[x]


def union(x):

    global flag

    par_x = find(x)
    print("x:", x, "par_x:", par_x)
    if par_x == x:
        par_xm = find(x-1)
        par[x] = par_xm
        return
    if par_x == 0:
        flag = True
        return
    y = par_x-1
    par_y = find(y)
    print("par_y:", par_y)
    if par_y == y and par_y != 0:
        par_ym = find(y-1)
        print("par_ym:", par_ym)
        par[par_x-1] = par_ym
        par[x] = par_ym
    else:
        par[x] = par_y


if __name__ == "__main__":
    g = int(input())
    p = int(input())
    par = [i for i in range(g+1)]
    flag = False
    count = 0
    for _ in range(p):
        union(int(input()))
        print_list_pretty([i for i in range(g+1)], 2)
        print_list_pretty(par, 2)
        print(flag)
        if flag:
            break
        count += 1

    print(count)
