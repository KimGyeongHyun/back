from sys import stdin
import heapq


if __name__ == "__main__":
    n = int(stdin.readline())

    data = int(stdin.readline())

    min_heap = []
    max_heap = []
    heapq.heappush(max_heap, -data)
    print(data)

    for i in range(1, n):

        data = int(stdin.readline())

        if i % 2 == 0:
            heapq.heappush(max_heap, -data)
        else:
            heapq.heappush(min_heap, data)

        if -max_heap[0] > min_heap[0]:
            t1 = -heapq.heappop(max_heap)
            t2 = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -t2)
            heapq.heappush(min_heap, t1)

        print(-max_heap[0])
