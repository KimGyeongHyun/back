import heapq
import matplotlib.pyplot as plt


def print_2d_array(l):
    """2차원 배열 출력"""
    for line in l:
        if not line:
            print("None")
            continue
        print(*line)


def print_2d_array_avoid_0(l):
    """2차원 배열 첫번째 인덱스를 제거하고 출력"""
    for line in l[1:]:
        if not line:
            print("None")
            continue
        print(*line)


def print_2d_array_avoid_00(l):
    """2차원 배열 모든 첫번째 인덱스를 제거하고 출력"""
    for line in l[1:]:
        if not line[1:]:
            print("None")
            continue
        print(*line[1:])


def see_heapq(l):
    """힙을 깊은 복사하여 순서대로 출력"""

    if not l:
        print("empty")
        return

    t = l[:]
    while True:
        print(heapq.heappop(t), end='')
        if t:
            print(end=', ')
        else:
            print()
            break


def draw_l_line(l):
    for i in range(len(l)):
        plt.hlines(i+1, l[i][0], l[i][1], color='blue')
    plt.show()