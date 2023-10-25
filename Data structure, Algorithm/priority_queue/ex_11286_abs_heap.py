from sys import stdin
import heapq


if __name__ == "__main__":
    n = int(stdin.readline())
    p_heap = []

    for _ in range(n):

        i = int(stdin.readline())

        if i == 0:
            if len(p_heap) == 0:
                print(0)
            else:
                print(heapq.heappop(p_heap)[1])

            continue

        heapq.heappush(p_heap, (abs(i), i))

