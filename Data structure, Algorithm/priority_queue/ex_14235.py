from sys import stdin
import heapq
gift = []


def pop_gift():

    if not gift:
        return -1

    return -heapq.heappop(gift)


if __name__ == "__main__":
    n = int(stdin.readline())

    for _ in range(n):
        l = list(map(int, stdin.readline().split()))

        if l[0] == 0:
            print(pop_gift())
            continue

        for i in range(1, l[0]+1):
            heapq.heappush(gift, -l[i])
