from sys import stdin
import heapq
# from my_lib.tools import *

# n이 1500 일 때 2차 배열 메모리는 9MB, 메모리 제한이 12MB
# 따라서 인풋 데이터를 그대로 받아오기만 해도 메모리 초과가 발생할 수 있다

# 우선순위 큐는 데이터의 정렬을 유지하면서 삽입, 삭제에 특화 되어 있다
# n 번째로 큰 수를 구하면 되므로 우선순위 큐의 크기를 n개로 유지하면서 모든 데이터를 받으면 된다
# 그러면 n**2 였던 메모리복잡도를 n 으로 줄일 수 있다

if __name__ == "__main__":
    n = int(stdin.readline())
    t = list(map(int, stdin.readline().split()))
    # l : 우선순위 큐, 최소 힙
    l = []
    # 우선 첫번째 줄의 n개의 수를 우선순위 큐에 삽입
    for num in t:
        heapq.heappush(l, num)

    # 나머지 수에 대해 push, pop 반복
    # l 이 n개의 수 유지되면서 제일 작은 값이 제거됨
    # 마지막에는 n 번째로 큰 수가 l 의 최상단 노드에 남아있게 된다
    for _ in range(n-1):
        t = list(map(int, stdin.readline().split()))
        for num in t:
            heapq.heappush(l, num)
            heapq.heappop(l)
        # see_heapq(l)
    print(heapq.heappop(l))