import sys
input = sys.stdin.readline

# *를 n*n 크기에 모두 칠한다
# 이후 규칙성에 따라 *를 제거한다

# 규칙
# 가운데 가로, 세로 1/3 ~ 2/3 부분의 *를 제거한다
# 가로,세로가 3으로 나뉜 9개의 영역에서 다시 가운데 *를 제거한다
# 반복한다


def del_star(l, row, col, n):
    # row, col : 제거를 실행할 시작 인덱스 값
    # n : 제거할 배열의 가로, 세로 크기
    # (row, col) 기준으로 n 의 1/3 ~ 2/3 부분의 *가 제거된다

    if n == 1:
        return

    gap = n//3

    # * 제거
    for i in range(gap, 2 * gap):
        for j in range(gap, 2 * gap):
            l[row + i][col + j] = ' '

    # 9개의 영역에서 재귀 호출
    for i in range(3):
        for j in range(3):
            del_star(l, row + i*gap, col + j*gap, n//3)


if __name__ == "__main__":
    n = int(input())

    l = [['*' for _ in range(n)] for _ in range(n)]

    del_star(l, 0, 0, n)

    for line in l:
        print("".join(line))
