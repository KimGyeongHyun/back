import sys
input = sys.stdin.readline

# False 부터 시작해서 하나씩 True 로 채우는 방식 사용
# 기울기를 모두 체크해보며, 이미 해당 기울기를 체크했다면 넘어가는 방식
# 배열의 모든 인덱스를 체크하며 넘어가기엔 시간복잡도가 너무 크기 때문에
# 유효한 기울기가 발견 되었다면 +1 씩 추가하는 방식 사용


MAX_INDEX = 1000
cnt = 0
res = [0] * (MAX_INDEX+1)
chk = [[False] * (MAX_INDEX+1) for _ in range(MAX_INDEX+1)]


def set(a, b):
    """a, b 방향의 직선의 점을 모두 True 로 바꾸는 메소드"""
    global chk
    x, y = a, b
    while x <= MAX_INDEX and y <= MAX_INDEX:
        chk[x][y] = True
        x += a
        y += b


def mul_set():
    """모든 기울기를 찾고 res 배열에 갱신"""
    global cnt, res, chk
    # x = y 축으로 대칭이기 때문에 x 는 n 까지만 탐색
    for n in range(1, MAX_INDEX+1):
        y = n
        for x in range(1, n):
            # 해당 기울기를 이미 체크했으면 그냥 넘어감
            if chk[x][y]:
                continue
            # 아니라면 해당 기울기의 모든 점을 체크하고 카운트를 올림
            set(x, y)
            cnt += 1
        # (1, 0), (1, 1), (0, 1)
        res[n] = 2*cnt + 3


if __name__ == "__main__":
    mul_set()

    t = int(input())
    for _ in range(t):
        print(res[int(input())])
