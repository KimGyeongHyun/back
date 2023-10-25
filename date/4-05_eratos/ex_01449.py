from sys import stdin
from collections import deque


if __name__ == "__main__":
    n, l = map(int, stdin.readline().split())
    a = list(map(int, stdin.readline().split()))
    a.sort()
    queue = deque(a)

    count = 0

    while True:

        if len(queue) == 0:
            break

        start = queue.popleft()
        count += 1

        while True:

            if len(queue) == 0:
                break
            end = queue[0]
            if end - start >= l:
                break
            queue.popleft()

    print(count)
