from sys import stdin
import heapq

# 2개의 합칠 카드를 고를 때 제일 작은 두 카드를 골라야 한다
# 따라서 정렬을 유지하면서 삽입, 삭제가 용이한 우선순위 큐를 사용

# 제일 작은 두 카드를 뽑고 더한 후 더한 값을 가진 카드를 2개 추가
# '최소 힙에서 카드 2개 pop, 합친 값을 2번 추가' 이를 m번 반복한다

if __name__ == "__main__":
    n, m = map(int, stdin.readline().split())
    t = list(map(int, stdin.readline().split()))
    l = []
    for num in t:
        heapq.heappush(l, num)

    for _ in range(m):
        f, s = heapq.heappop(l), heapq.heappop(l)
        for _ in range(2):
            heapq.heappush(l, f+s)

    print(sum(l))