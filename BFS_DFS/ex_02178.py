from sys import stdin


count = 0


def DFS_maze(x, y, n, m, c, visit):

    global count

    visit[x][y] = True

    if x == n-1 and y == m-1:
        if c < count:
            count = c
        return

    if 1 <= x and not visit[x-1][y]:
        DFS_maze(x-1, y, n, m, c+1, visit)
    if x <= m-2 and not visit[x+1][y]:
        DFS_maze(x+1, y, n, m, c+1, visit)
    if 1 <= y and not visit[x][y-1]:
        DFS_maze(x, y-1, n, m, c+1, visit)
    if y <= n-2 and not visit[x][y+1]:
        DFS_maze(x, y+1, n, m, c+1, visit)


if __name__ == "__main__":

    global count

    n, m = map(int, input().split())
    count = n + m

    maze = []

    for _ in range(n):
        line = list(map(int, stdin.readline()[:-1]))
        maze.append(line)

    # for line in maze:
    #     print(line)

    is_visit = [[False for _ in range(m)] for _ in range(n)]

    DFS_maze(0, 0, n, m, 0, is_visit)
    print(count)



