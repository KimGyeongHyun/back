from sys import stdin
import heapq

if __name__ == "__main__":
    n = int(stdin.readline())
    heap = []
    for _ in range(n):
        heapq.heappush(heap, int(stdin.readline()))

    for _ in range(n):
        print(heapq.heappop(heap))

