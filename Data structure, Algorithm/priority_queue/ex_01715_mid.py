from sys import stdin
import heapq
# from my_lib.tools import *

# 카드 뭉치가 n개 있으면 n-1 횟수 만큼 더한다
# 카드 뭉치가 제일 작은 것 두 개를 우선으로 더한다
# 삽입, 삭제 연산이 많고 정렬을 유지해야 하므로 우선순위 큐를 사용


if __name__ == "__main__":
    n = int(stdin.readline())
    l = []
    for _ in range(n):
        heapq.heappush(l, int(stdin.readline()))

    # see_heapq(l)

    total_sum = 0
    for _ in range(n-1):
        val = heapq.heappop(l) + heapq.heappop(l)
        heapq.heappush(l, val)
        total_sum += val

    # print(heapq.heappop(l))
    print(total_sum)