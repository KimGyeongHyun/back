import heapq
import matplotlib.pyplot as plt


def print_2d_array(l):
    """2차원 배열 출력"""
    for line in l:
        print(*line)


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