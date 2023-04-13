from sys import stdin
from collections import deque

# 처음에 DFS 로 시도했으나 적합하지 않다고 판단하고 이후 BFS 를 시도했다
# 주변 상하좌우 4칸을 한꺼번에 확장하고 count + 1 한다
# 제일 마지막 칸에 도달했을 때 해당 count 가 최소 이동 거리가 된다


def BFS_maze(n, m, maze):
    # 방문 여부 검사
    is_visit = [[False for _ in range(m)] for _ in range(n)]
    is_visit[0][0] = True   # 첫 칸은 방문

    d = deque()     # BFS 를 위한 데크

    # y, x, 해당 칸 최소 이동 거리
    d.append((0, 0, 1))

    while d:
        y, x, c = d.popleft()

        # 미로 방문 여부 출력
        # print(c)
        # for i in range(n):
        #     for j in range(m):
        #         if is_visit[i][j]:
        #             print("1", end="")
        #         else:
        #             print("0", end="")
        #     print()
        # print()

        # 해당 칸이 마지막 칸이라면 해당 최소 이동 거리 반환
        if x == m-1 and y == n-1:
            return c

        # 방문할 수 있는 칸을 모두 탐색
        # 최단 이동 거리 + 1
        if x >= 1 and maze[y][x-1] == 1 and not is_visit[y][x-1]:
            d.append((y, x-1, c+1))
            is_visit[y][x-1] = True
        if x <= m-2 and maze[y][x+1] == 1 and not is_visit[y][x+1]:
            d.append((y, x+1, c+1))
            is_visit[y][x+1] = True
        if y >= 1 and maze[y-1][x] == 1 and not is_visit[y-1][x]:
            d.append((y-1, x, c+1))
            is_visit[y-1][x] = True
        if y <= n-2 and maze[y+1][x] == 1 and not is_visit[y+1][x]:
            d.append((y+1, x, c+1))
            is_visit[y+1][x] = True


if __name__ == "__main__":

    n, m = map(int, input().split())

    maze = []

    for _ in range(n):
        line = list(map(int, stdin.readline()[:-1]))
        maze.append(line)

    # 미로 출력
    # for line in maze:
    #     print(line)

    print(BFS_maze(n, m, maze))
