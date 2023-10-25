from sys import stdin
from collections import deque

# 1) subin = 0 일 때 무한 루프
# 2) subin == k 이 탈출 조건이 아님
# 3) visit 은 2의 배수로 모두 적용해야 함
# 4) 처음 n이 0일 때 None 이 반환됨

def get_smallest_time(n, k):

    if k < n:
        return n - k

    d = deque()
    d.append((n, 0))
    visit = [False for _ in range(100001)]
    visit[n] = True

    while d:

        subin, time = d.popleft()
        # print(subin, time)

        if subin == k == 0:
            return time

        # 1), 4)
        if subin == 0:
            d.append((1, time+1))
            continue

        # 2)
        comp = subin
        while comp <= 100000:
            # 4)
            visit[comp] = True
            if comp == k:
                return time
            comp *= 2

        while subin-1 <= 100000:

            if subin-1 >= 0 and not visit[subin-1]:
                d.append((subin-1, time+1))

            if subin+1 <= 100000 and not visit[subin+1]:
                d.append((subin+1, time+1))

            subin *= 2


if __name__ == "__main__":
    n, k = map(int, stdin.readline().split())
    print(get_smallest_time(n, k))