import heapq


def print_2d_array(l):
    """2차원 배열 출력"""
    for line in l:
        print(*line)


def see_heapq(l):
    """힙을 깊은 복사하여 순서대로 출력"""
    t = l[:]
    while True:
        print(heapq.heappop(t), end='')
        if t:
            print(end=', ')
        else:
            print()
            break
