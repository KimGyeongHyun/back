import sys
sys.setrecursionlimit(10**5)

count = 0


# def print_cab(cab):
#     x_len = len(cab)
#     y_len = len(cab[0])
#
#     print("===============")
#
#     for y in range(y_len):
#         for x in range(x_len):
#             if cab[x][y][1] is True:
#                 print("■ ", end='')
#             else:
#                 print("□ ", end='')
#         print()
#     print("=================\n")

def search(cab, x, y):
    # print("x, y : {}, {}".format(x, y))

    x_len = len(cab)
    y_len = len(cab[0])

    cab[x][y][1] = True

    # print_cab(cab)

    if cab[x][y][0] == 1:

        if 1 <= x and cab[x-1][y][1] is False:
            search(cab, x-1, y)
        if x <= x_len - 2 and cab[x+1][y][1] is False:
            search(cab, x+1, y)
        if 1 <= y and cab[x][y-1][1] is False:
            search(cab, x, y-1)
        if y <= y_len - 2 and cab[x][y+1][1] is False:
            search(cab, x, y+1)


def increase_count(cab, x, y):

    if cab[x][y][1] is True:
        return

    # print("start x, y : {}, {}".format(x, y))
    global count
    search(cab, x, y)
    count += 1
    # print("recurr end")


if __name__ == "__main__":
    t = int(sys.stdin.readline())

    for _ in range(t):
        count = 0
        m, n, k = map(int, sys.stdin.readline().split())
        cab = [[[0, False] for _ in range(n)] for _ in range(m)]

        for __ in range(k):
            x, y = map(int, sys.stdin.readline().split())
            cab[x][y][0] = 1

        for x in range(m):
            for y in range(n):
                if cab[x][y][0] == 1:
                    increase_count(cab, x, y)

        print(count)

